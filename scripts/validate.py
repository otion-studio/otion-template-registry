#!/usr/bin/env python3
"""
Otion template registry validator.

Run against the repo root. Checks every template under templates/ for:

  MANIFEST   template.json present, valid, matches schemas/template.schema.json
             (field-by-field, no external deps).
  WORKSPACE  The workspace/ folder is a valid Otion workspace fragment:
             markers parse, databases have the right shape, select values
             match options, _parent_id and cross-db refs resolve, no
             deprecated types, no forbidden Markdown.
  SECURITY   No remote embeds (file/iconImage src and frontmatter cover must
             be workspace-relative, no URL schemes), no path traversal, no
             symlinks, only allowed file extensions, no app-generated files
             (project.otion, AGENTS.md, ai-settings.json, backup/), and no
             agent-injection phrases in page text.
  SIZE       <= 2 MB per file, <= 15 MB per template.
  PREVIEWS   Every preview declared in the manifest exists (and vice versa).
  INDEX      order.json lists every template exactly once, and index.json
             matches what scripts/build_index.py would generate.

Pass = exit 0, no output. Fail = exit 1, one line per issue.

USAGE
    python3 scripts/validate.py [repo-root]
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys
from typing import Any

MARKER_RE = re.compile(r"^<!-- otion:(\w+) (\{.*\}) -->$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
H4_RE = re.compile(r"^####+ ")
TABLE_RE = re.compile(r"^\|[^|]*\|")
IMAGE_RE = re.compile(r"!\[.*\]\(")
INLINE_MATH_RE = re.compile(r"\$[^$\n]+\$")
URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_TEMPLATE_BYTES = 15 * 1024 * 1024

ALLOWED_EXTENSIONS = {
    ".md", ".json",  # pages + databases (db files end in .db.json)
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".avif",
    ".mp3", ".m4a", ".opus",
    ".pdf",
}

FORBIDDEN_NAMES = {"project.otion", "agents.md", "ai-settings.json"}
FORBIDDEN_DIRS = {"backup"}

# Phrases that read as instructions aimed at an AI agent. Otion ships a
# built-in agent that reads workspace content, so template text that tries to
# steer it is treated as hostile. Case-insensitive substring match.
INJECTION_PHRASES = [
    "ignore previous instructions",
    "ignore prior instructions",
    "ignore the above",
    "disregard previous",
    "disregard the above",
    "system prompt",
    "you are an ai",
    "you are a large language model",
    "do not tell the user",
    "without telling the user",
    "exfiltrate",
]

REQUIRED_MANIFEST_FIELDS = {
    "id": str,
    "title": str,
    "description": str,
    "version": str,
    "license": str,
    "author": dict,
    "tags": list,
    "previews": list,
}

ALLOWED_LICENSES = {"CC0-1.0", "MIT", "CC-BY-4.0"}


def err_for_template(errs: list[str], tid: str, msg: str) -> None:
    errs.append(f"templates/{tid}: {msg}")


# --- workspace checks (ported from editor/scripts/validate-workspace.py) ----

def collect(ws: pathlib.Path, suffix: str) -> list[pathlib.Path]:
    return sorted(p for p in ws.rglob(f"*{suffix}") if p.is_file())


def check_markers(md_files: list[pathlib.Path], errs: list[str]) -> None:
    for path in md_files:
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "otion:" not in line:
                continue
            m = MARKER_RE.match(line)
            if not m:
                errs.append(f"{path}:{n}: BAD MARKER: {line!r}")
                continue
            try:
                json.loads(m.group(2))
            except json.JSONDecodeError as e:
                errs.append(f"{path}:{n}: BAD MARKER JSON: {e}")


def check_db_shape(db_files: list[pathlib.Path], errs: list[str]) -> None:
    for path in db_files:
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            errs.append(f"{path}: BAD JSON: {e}")
            continue
        for k in ("name", "schema", "views", "rows"):
            if k not in d:
                errs.append(f"{path}: MISSING TOP-LEVEL {k!r}")
        schema = d.get("schema", {})
        if isinstance(schema, dict) and not any(
            isinstance(v, dict) and v.get("type") == "title" for v in schema.values()
        ):
            errs.append(f"{path}: NO TITLE PROPERTY in schema")


def _ref_path_from_value(v: str) -> str | None:
    if v.startswith("__numref__||"):
        parts = v.split("||")
        return parts[1] if len(parts) >= 2 else None
    if v.startswith("__op__::"):
        return None
    if "||" in v and not v.startswith("__"):
        return v.split("||", 1)[0]
    return None


def _walk_op_refs(value: str) -> list[str]:
    if not value.startswith("__op__::"):
        return []
    try:
        op = json.loads(value[len("__op__::"):])
    except Exception:
        return []
    paths: list[str] = []
    stack: list[Any] = [op.get("a"), op.get("b")]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            if o.get("type") == "ref" and isinstance(o.get("path"), str):
                paths.append(o["path"])
            stack.extend([o.get("a"), o.get("b")])
    return paths


def check_db_integrity(db_files: list[pathlib.Path], errs: list[str]) -> None:
    for path in db_files:
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        base = path.parent
        schema = d.get("schema", {})
        select_opts = {
            k: {o["name"] for o in (p.get("options") or []) if "name" in o}
            for k, p in schema.items()
            if isinstance(p, dict) and p.get("type") in ("select", "multi_select")
        }
        row_ids = {r.get("id") for r in d.get("rows", [])}
        seen_ids: set[str] = set()

        for r in d.get("rows", []):
            rid = r.get("id")
            if not rid:
                errs.append(f"{path}: row without id")
            elif rid in seen_ids:
                errs.append(f"{path}: duplicate row id {rid!r}")
            seen_ids.add(rid)

            for k, allowed in select_opts.items():
                v = r.get(k)
                if v in ("", None):
                    continue
                if isinstance(v, list):
                    bad = [x for x in v if x not in allowed]
                    if bad:
                        errs.append(f"{path}: row {rid!r} {k!r}: invalid multi-select {bad}")
                elif v not in allowed:
                    errs.append(f"{path}: row {rid!r} {k!r}: {v!r} not in {sorted(allowed)}")

            pid = r.get("_parent_id")
            if pid and pid not in row_ids:
                errs.append(f"{path}: row {rid!r} has dangling _parent_id={pid!r}")

        def file_exists(rel: str) -> bool:
            return (base / rel).resolve().exists()

        for k, p in schema.items():
            if isinstance(p, dict):
                rd = p.get("ref_db")
                if isinstance(rd, str) and rd and not file_exists(rd):
                    errs.append(f"{path}: schema[{k!r}].ref_db -> missing {rd!r}")

        for r in d.get("rows", []):
            for k, v in r.items():
                if not isinstance(v, str) or not v:
                    continue
                rel = _ref_path_from_value(v)
                if rel and not file_exists(rel):
                    errs.append(f"{path}: row {r.get('id')!r} {k!r}: ref -> missing {rel!r}")
                for rel2 in _walk_op_refs(v):
                    if not file_exists(rel2):
                        errs.append(f"{path}: row {r.get('id')!r} {k!r}: op ref -> missing {rel2!r}")


def check_md_strict(md_files: list[pathlib.Path], db_files: list[pathlib.Path], errs: list[str]) -> None:
    for path in db_files:
        text = path.read_text(encoding="utf-8")
        if re.search(r'"type"\s*:\s*"status"', text):
            errs.append(f"{path}: deprecated property type 'status' (use 'select')")
        if re.search(r'"type"\s*:\s*"list"', text):
            errs.append(f"{path}: deprecated view type 'list' (use 'table')")
    for path in md_files:
        in_fence = False
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if H4_RE.match(line):
                errs.append(f"{path}:{n}: H4+ heading (not supported)")
            if TABLE_RE.match(line):
                errs.append(f"{path}:{n}: Markdown table (use a database)")
            if IMAGE_RE.search(line) and "<!-- otion:" not in line:
                errs.append(f"{path}:{n}: inline image syntax (use otion:file block)")
            if INLINE_MATH_RE.search(line):
                errs.append(f"{path}:{n}: inline math (use otion:math block)")


# --- security checks ---------------------------------------------------------

def check_security(tid: str, ws: pathlib.Path, errs: list[str]) -> None:
    total = 0
    for p in sorted(ws.rglob("*")):
        rel = p.relative_to(ws)
        if p.is_symlink():
            err_for_template(errs, tid, f"symlink not allowed: {rel}")
            continue
        if p.is_dir():
            if p.name.lower() in FORBIDDEN_DIRS or p.name.startswith("."):
                err_for_template(errs, tid, f"forbidden directory: {rel}")
            continue
        if p.name.lower() in FORBIDDEN_NAMES or p.name.startswith("."):
            err_for_template(errs, tid, f"app-generated or hidden file not allowed: {rel}")
        ext = p.suffix.lower()
        name = p.name.lower()
        if not (name.endswith(".db.json") or ext in ALLOWED_EXTENSIONS):
            err_for_template(errs, tid, f"file type not allowed: {rel}")
        if ".." in rel.parts:
            err_for_template(errs, tid, f"path traversal in filename: {rel}")
        size = p.stat().st_size
        total += size
        if size > MAX_FILE_BYTES:
            err_for_template(errs, tid, f"file too large ({size} bytes, max {MAX_FILE_BYTES}): {rel}")
    if total > MAX_TEMPLATE_BYTES:
        err_for_template(errs, tid, f"template too large ({total} bytes, max {MAX_TEMPLATE_BYTES})")

    # Remote embeds + traversal inside markers and frontmatter
    for path in collect(ws, ".md"):
        text = path.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            m = MARKER_RE.match(line)
            if m:
                try:
                    props = json.loads(m.group(2))
                except Exception:
                    continue
                for key in ("src", "path", "cover"):
                    v = props.get(key)
                    if isinstance(v, str) and v:
                        if URL_SCHEME_RE.match(v):
                            err_for_template(errs, tid, f"{path.relative_to(ws)}:{n}: remote {key} not allowed: {v!r}")
                        if v.startswith("/") or ".." in v.split("/"):
                            err_for_template(errs, tid, f"{path.relative_to(ws)}:{n}: non-relative {key}: {v!r}")
            if line.startswith("cover:"):
                v = line.split(":", 1)[1].strip()
                if URL_SCHEME_RE.match(v):
                    err_for_template(errs, tid, f"{path.relative_to(ws)}:{n}: remote cover not allowed")
        lowered = text.lower()
        for phrase in INJECTION_PHRASES:
            if phrase in lowered:
                err_for_template(errs, tid, f"{path.relative_to(ws)}: agent-injection phrase {phrase!r}")


# --- manifest ----------------------------------------------------------------

def check_manifest(tid: str, tdir: pathlib.Path, errs: list[str]) -> dict | None:
    mf = tdir / "template.json"
    if not mf.exists():
        err_for_template(errs, tid, "missing template.json")
        return None
    try:
        m = json.loads(mf.read_text(encoding="utf-8"))
    except Exception as e:
        err_for_template(errs, tid, f"template.json bad JSON: {e}")
        return None
    for field, typ in REQUIRED_MANIFEST_FIELDS.items():
        if field not in m:
            err_for_template(errs, tid, f"template.json missing {field!r}")
        elif not isinstance(m[field], typ):
            err_for_template(errs, tid, f"template.json {field!r} must be {typ.__name__}")
    if m.get("id") != tid:
        err_for_template(errs, tid, f"template.json id {m.get('id')!r} != folder name")
    if isinstance(m.get("id"), str) and not ID_RE.match(m["id"]):
        err_for_template(errs, tid, "id must be lowercase kebab-case")
    if isinstance(m.get("author"), dict) and not isinstance(m["author"].get("name"), str):
        err_for_template(errs, tid, "author.name required")
    if m.get("license") not in ALLOWED_LICENSES:
        err_for_template(errs, tid, f"license must be one of {sorted(ALLOWED_LICENSES)}")
    if isinstance(m.get("description"), str) and len(m["description"]) > 200:
        err_for_template(errs, tid, "description over 200 chars")

    previews = m.get("previews")
    if isinstance(previews, list):
        if not previews:
            err_for_template(errs, tid, "at least one preview required")
        declared = set()
        for p in previews:
            declared.add(p)
            if not isinstance(p, str) or not (tdir / "preview" / p).is_file():
                err_for_template(errs, tid, f"declared preview missing: preview/{p}")
        pdir = tdir / "preview"
        if pdir.is_dir():
            for f in pdir.iterdir():
                if f.is_file() and f.name not in declared:
                    err_for_template(errs, tid, f"undeclared file in preview/: {f.name}")
    return m


# --- index -------------------------------------------------------------------

def list_workspace_files(ws: pathlib.Path) -> list[str]:
    """Every regular file under workspace/, as forward-slash paths relative to
    workspace/, sorted. This is the explicit manifest the client fetches —
    clients never glob the repo tree, they only fetch files declared here."""
    files = []
    for p in sorted(ws.rglob("*")):
        if p.is_file() and not p.is_symlink():
            files.append(p.relative_to(ws).as_posix())
    return files


def build_index(root: pathlib.Path) -> dict:
    order_file = root / "order.json"
    order = json.loads(order_file.read_text(encoding="utf-8"))["order"]
    entries = []
    for tid in order:
        m = json.loads((root / "templates" / tid / "template.json").read_text(encoding="utf-8"))
        entries.append({
            "id": m["id"],
            "title": m["title"],
            "description": m["description"],
            "version": m["version"],
            "license": m["license"],
            "author": m["author"],
            "tags": m["tags"],
            "previews": [f"templates/{tid}/preview/{p}" for p in m["previews"]],
            "path": f"templates/{tid}/workspace",
            "files": list_workspace_files(root / "templates" / tid / "workspace"),
        })
    return {"version": 1, "templates": entries}


def check_index(root: pathlib.Path, template_ids: list[str], errs: list[str]) -> None:
    order_file = root / "order.json"
    if not order_file.exists():
        errs.append("order.json missing")
        return
    try:
        order = json.loads(order_file.read_text(encoding="utf-8"))["order"]
    except Exception as e:
        errs.append(f"order.json invalid: {e}")
        return
    if sorted(order) != sorted(template_ids):
        errs.append(
            f"order.json out of sync: order={sorted(order)} folders={sorted(template_ids)}"
        )
        return
    index_file = root / "index.json"
    if not index_file.exists():
        errs.append("index.json missing — run scripts/build_index.py")
        return
    try:
        on_disk = json.loads(index_file.read_text(encoding="utf-8"))
    except Exception as e:
        errs.append(f"index.json invalid: {e}")
        return
    if on_disk != build_index(root):
        errs.append("index.json stale — run scripts/build_index.py and commit the result")


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    tdir = root / "templates"
    if not tdir.is_dir():
        print("error: templates/ not found — run from the repo root", file=sys.stderr)
        return 2

    errs: list[str] = []
    template_ids = sorted(p.name for p in tdir.iterdir() if p.is_dir())
    for tid in template_ids:
        t = tdir / tid
        check_manifest(tid, t, errs)
        ws = t / "workspace"
        if not ws.is_dir():
            err_for_template(errs, tid, "missing workspace/ folder")
            continue
        md = collect(ws, ".md")
        db = collect(ws, ".db.json")
        if not md and not db:
            err_for_template(errs, tid, "workspace/ has no pages or databases")
        check_markers(md, errs)
        check_db_shape(db, errs)
        check_db_integrity(db, errs)
        check_md_strict(md, db, errs)
        check_security(tid, ws, errs)

    check_index(root, template_ids, errs)

    for e in errs:
        print(e)
    return 0 if not errs else 1


if __name__ == "__main__":
    sys.exit(main())

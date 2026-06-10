# Otion Template Registry

This repository is the source of truth for the workspace templates shown in Otion's "New from template" gallery.

A template is just what Otion is: **a folder of plain files.** Each entry here holds a small manifest, a square gallery icon, and the workspace files themselves — Markdown pages, `.db.json` databases, and any local assets (images, audio, PDFs).

## Security

**Every template is scanned for security before it can be listed, and re-scanned on every change.** CI rejects any template that contains remote embeds or network references, path traversal, symlinks, hidden or app-generated files, disallowed file types, oversized files, or text that attempts to instruct the user's AI agent (prompt injection). Templates are data, not code — nothing in a template executes — and the scan keeps it that way. A human maintainer additionally reviews every submission before merge.

## What's in this repo

| Path | Purpose |
|---|---|
| [`index.json`](index.json) | The generated gallery index Otion clients fetch. Never edit by hand. |
| [`order.json`](order.json) | Display order. Maintainer-controlled — contributor PRs must not touch it. |
| [`templates/<id>/template.json`](schemas/template.schema.json) | Per-template manifest (title, description, author, version, license, tags, icon). |
| `templates/<id>/icon.png` | Square (1:1) icon shown in the gallery, ≤ 512 KB. Never copied into a user's workspace. |
| `templates/<id>/workspace/` | The template content: pages, `databases/`, assets. |
| [`scripts/validate.py`](scripts/validate.py) | The full validation + security scan CI runs. Run it locally before submitting. |
| [`scripts/build_index.py`](scripts/build_index.py) | Regenerates `index.json` from the manifests + `order.json`. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to submit, update, or remove a template. |

## How it works

1. An author adds a folder under `templates/` and opens a pull request (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
2. CI validates the workspace format and runs the security scan. Red CI = no review.
3. A maintainer reviews for quality and taste, adds the id to `order.json`, regenerates `index.json`, and merges.
4. Otion clients fetch `index.json` from `main` and download template files on demand. Instantiating a template copies the files into a new local workspace — after that, the user owns them outright.

Updates and removals are also pull requests. Everything is a reviewable diff; there is no admin panel and no off-record state.

## What a template folder must NOT contain

App-generated files are created by Otion at instantiation time and are rejected by the scan: `project.otion`, `AGENTS.md`, `ai-settings.json`, `backup/`, and anything dot-prefixed. A template is only the unique content.

## Licensing

Template manifests must declare a permissive license (`CC0-1.0`, `MIT`, or `CC-BY-4.0`) — when a user instantiates a template, the files belong to them. The registry tooling is MIT.

#!/usr/bin/env python3
"""
Regenerate index.json from templates/*/template.json, ordered by order.json.

Maintainers control display order by editing order.json; contributors never
touch index.json directly. CI fails if index.json doesn't match this output.

USAGE
    python3 scripts/build_index.py [repo-root]
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate import build_index  # noqa: E402


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    index = build_index(root)
    out = root / "index.json"
    out.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(index['templates'])} templates)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

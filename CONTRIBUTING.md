# Contributing a template

## Submit

1. Build your workspace in Otion until it looks the way you want.
2. Copy the content files into `templates/<your-id>/workspace/` — pages (`.md`), `databases/`, and any local assets. **Do not include** `project.otion`, `AGENTS.md`, `ai-settings.json`, `backup/`, or dot-files; Otion generates those.
3. Add `templates/<your-id>/template.json` following [`schemas/template.schema.json`](schemas/template.schema.json). Title with the use case ("Plan and ship a project"), not the feature ("Board view").
4. Add at least one screenshot to `templates/<your-id>/preview/` and list it in the manifest.
5. Run the validator from the repo root and fix anything it reports:

   ```bash
   python3 scripts/validate.py
   ```

   (It will report `order.json out of sync` for your new id — that's expected; a maintainer handles ordering on merge. Everything else must pass.)
6. Open a pull request that touches **only** `templates/<your-id>/`. Do not edit `order.json` or `index.json`.

## Rules

- **Self-contained.** All assets are local files inside the template. No remote images, no network references of any kind.
- **No agent steering.** Page text must not contain instructions aimed at AI agents. The scan rejects known injection phrases; reviewers reject creative ones.
- **Size.** ≤ 2 MB per file, ≤ 15 MB per template. Use compressed formats (webp/jpeg, m4a/mp3).
- **Format.** The workspace must pass the validator: clean markers, valid database shape, resolving references, no deprecated types. The authoritative format spec ships in every Otion workspace as `AGENTS.md`.
- **License.** `CC0-1.0`, `MIT`, or `CC-BY-4.0` only. Users own what they instantiate.
- **Content.** Original work or content you have the right to publish. Nothing offensive, no advertising, placeholder text in the user's interest (realistic example data beats lorem ipsum).

## Update or remove your template

Open another PR. For updates, bump `version` in your manifest. For removal, delete your folder — a maintainer drops the id from `order.json` and regenerates the index. Users who already instantiated your template keep their copies; removal only delists it.

## Review

CI must be green before review starts. Maintainers review for quality and curation fit, and control listing and ordering (`order.json`). Decisions about what gets in and in what order are at the maintainers' discretion.

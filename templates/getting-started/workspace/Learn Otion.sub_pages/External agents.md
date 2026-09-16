---
title: External agents
icon: FileCode
---

# External agents

Open this workspace folder in Claude Code, Codex, or another agent with local file access. Point it to agents.readme.md. The skillsandtools folder contains portable format guides, schemas, examples, and verification scripts.

Otion has no built-in model, chat sidebar, or provider-key setup. A chat-only agent needs you to supply the relevant files and run checks yourself.

## What to try first

- Ask your external agent to summarize the Inbox into three priorities.
- Ask it to create a Groceries database using the documented format.
- Save reusable instructions on a page, then use Copy to send them to your external agent.

<!-- otion:routine {"prompt":"Read agents.readme.md. Review the First Steps database. For every row still in Todo, suggest the single quickest action to complete it. Validate any changed files before reporting completion.","label":"Nudge me along","collapsed":"true"} -->

## Verify and share

Run the read-only validation commands in skillsandtools/README.md after changes. Review the diff before sharing and preserve both sides of any sync conflict. Settings → External agents can safely install or update the toolkit while preserving customized instructions.

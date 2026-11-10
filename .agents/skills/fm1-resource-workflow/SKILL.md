---
name: fm1-resource-workflow
description: Process links, GitHub issues, and pull requests for the FM-1 resource hub, including researched documentation updates and requested PR merges, using economical subagents.
---

# FM-1 resource workflow

Use this workflow when the user supplies a link or asks to process an issue or pull request for this repository. The user prefers inexpensive models for these straightforward tasks.

## Delegation

Delegate the bounded research or review to a subagent using `gpt-6-luna` with `low` reasoning effort when available. Give it the URL, task, and only the relevant context; ask for source links, concrete findings, and uncertainty. For a simple task use one subagent; use additional agents only for independent work that meaningfully saves time. The lead agent checks the result and completes the requested changes. If this model or delegation is unavailable, use the cheapest available suitable model or proceed directly; report the limitation rather than claiming a particular cost. Do not delegate external writes unless the user has authorized them.

## Source links and issues

Read the linked material and any relevant issue discussion. Verify material claims against the linked primary sources where possible, distinguish confirmed facts from claims or speculation, and do not invent details. If the source is inaccessible, report that and avoid presenting unverified information as fact.

Search `README.md` and `REVERSE_ENGINEERING.md` for the project, related links, and appropriate section before editing. Update an existing entry when appropriate instead of duplicating it. Put FM-1 firmware, tools, and community resources in the relevant README section; put hardware, protocol, and reverse-engineering details in the technical reference when appropriate. Follow the surrounding English, Markdown, table format, link style, and level of detail. Preserve the repository's FM-1 scope and distinguish related devices. Include useful source links and keep changes focused on supported information.

## Pull requests

Inspect the PR description, diff, discussion, review status, and relevant checks. Review the changes against the current repository and verify factual additions with their sources. Report actionable problems and address them only within the user's requested scope. When the user explicitly asks to merge, merge only after reviewing the current PR state and required checks; respect branch protection and do not bypass failing checks or unresolved blocking reviews. If merging is blocked, explain the specific blocker. Merely supplying a PR link or asking for review does not authorize merging.

## Finish

Inspect the resulting diff, check Markdown links and formatting affected by the edit, and run relevant checks if applicable. Summarize changes, sources, verification, and any unresolved uncertainty. Do not close issues, post comments, push, or merge unless requested or otherwise authorized.

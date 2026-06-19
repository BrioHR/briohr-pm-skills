# BrioHR PM Skills

A small set of [Agent Skills](https://support.anthropic.com/en/articles/skills) for **product managers at BrioHR**, designed to run in **Claude Desktop** and **Claude.ai (web)**. They turn rough product ideas into validated specs and engineering-ready user stories — tailored for HR-software work (multi-country, compliance, roles & permissions, approvals).

These are adapted from the open-source [Superpowers](https://github.com/obra/superpowers) methodology, with all engineering-only machinery (git, shell, sub-agents, hooks) removed so they work in the consumer Claude apps with no terminal.

## What's inside

| Skill | What it does | When it triggers |
|---|---|---|
| **feature-brainstorming** | Socratic discovery — asks one question at a time, proposes 2–3 approaches, then writes a structured spec. Can pull a Jira epic/ticket for context and post the spec back. | "I want to build a feature…", "help me scope…", "write a spec/PRD" |
| **ticket-writing** | Turns a feature/spec/Jira ticket into a single BrioHR-format story (Business Context, Behavior, User Flow, Other Considerations, Given/When/Then Acceptance Criteria), iterates with you, then offers to generate test cases. | "write a ticket", "write a user story", "acceptance criteria", "document this feature" |
| **generate-jira-test-cases** | Pulls a Jira ticket + context, walks you through a six-section QA checklist, and produces a developer-ready test case list. | "generate test cases for B2-1234", "prepare QA scenarios", "what should we test for this" |

> **Jira connector:** all three skills can use the Atlassian/Jira connector for ticket context. It's **required** for `generate-jira-test-cases` and **optional** for the other two (they work without it, just text-only). Connect Jira in Claude when prompted.

## Install (per PM, one-time)

Skills are installed individually in Claude.

### Claude Desktop / Claude.ai (web)
1. **Download the ready-to-upload zips** — grab them from the [latest Release](../../releases/latest):
   - `feature-brainstorming.zip`
   - `ticket-writing.zip`
   - `generate-jira-test-cases.zip` *(connect your Atlassian/Jira account when prompted)*
2. In Claude, go to **Settings → Capabilities → Skills** (you need a plan that supports custom Skills) and **upload** each zip.
3. The skills now trigger automatically based on what you ask — or invoke them by name.

> The zips already have `SKILL.md` at their root, so no zipping needed. To update a skill after we change it, just download the new zip and re-upload.

## How a PM uses them

```
Rough idea
   │  (feature-brainstorming)
   ▼
Approved Spec
   │  (ticket-writing)
   ▼
BrioHR-format ticket (story + acceptance criteria)  ──►  paste into Jira  ──►  ticket gets built
   │  (ticket-writing offers this once finalized, or run it directly)
   ▼  (generate-jira-test-cases)
QA test cases for the developer to verify
```

1. Describe your idea to Claude. `feature-brainstorming` kicks in, asks questions, and produces a spec.
2. Ask Claude to "write a ticket from this." `ticket-writing` produces a single BrioHR-format story, iterates with you, then offers to generate test cases.
3. `generate-jira-test-cases` gathers context, walks you through the six-section QA checklist, and outputs a test case list you can post back to the ticket.

### Use any skill on its own

The three skills are **independent — you can use one, two, or all three, in any order.** Install only the ones you want, and even with all three installed, each only activates when your request matches it:

- "Write a ticket for B2-1234" → only **ticket-writing** runs.
- "Generate test cases for B2-1234" → only **generate-jira-test-cases** runs.
- "Help me brainstorm a feature" → only **feature-brainstorming** runs.

The chain is opt-in: `feature-brainstorming` *offers* to hand off to `ticket-writing`, which *offers* to hand off to `generate-jira-test-cases`. If you say no, it stops — and if a downstream skill isn't installed, the offer simply leads nowhere. Nothing breaks. So a PM who already knows the feature can just use skills 2 + 3 (or skill 3 alone).

## Maintaining (for whoever edits the skills)

**Releases are automatic.** Every push to `main` triggers a GitHub Action
(`.github/workflows/release.yml`) that rebuilds the zips and publishes a new
release, bumping the minor version: `v1.0 → v1.1 → v1.2 → …`. So the only
maintenance step is:

```bash
git add -A && git commit -m "What changed" && git push
```

Within a minute, a new release with fresh zips appears at
[`/releases/latest`](../../releases/latest). PMs just re-download.

**To preview the zips locally before pushing** (the same ones the Action will build):

```bash
./scripts/build-zips.sh   # writes dist/*.zip (git-ignored)
```

The build script auto-discovers every folder under `skills/`, so new skills are
picked up automatically with no config.

## Customizing

The skills are plain Markdown. Edit the `SKILL.md` files to adjust personas, the spec template, or the compliance checklist to match how BrioHR actually works. The `description:` line in each file's frontmatter controls when Claude auto-triggers the skill — keep it specific.

## Contributing (BrioHR PMs)

1. Branch from `main`.
2. Edit the relevant `SKILL.md`.
3. Test it in your own Claude before opening a PR — paste a real feature idea and confirm the behavior.
4. Open a PR describing the real problem the change solves.

## Credit & License

Adapted from [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent (MIT). This repo is MIT licensed — see `LICENSE`.

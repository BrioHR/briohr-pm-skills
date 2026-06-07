# BrioHR PM Skills

A small set of [Agent Skills](https://support.anthropic.com/en/articles/skills) for **product managers at BrioHR**, designed to run in **Claude Desktop** and **Claude.ai (web)**. They turn rough product ideas into validated specs and engineering-ready user stories — tailored for HR-software work (multi-country, compliance, roles & permissions, approvals).

These are adapted from the open-source [Superpowers](https://github.com/obra/superpowers) methodology, with all engineering-only machinery (git, shell, sub-agents, hooks) removed so they work in the consumer Claude apps with no terminal.

## What's inside

| Skill | What it does | When it triggers |
|---|---|---|
| **feature-brainstorming** | Socratic discovery — asks one question at a time, proposes 2–3 approaches, then writes a structured spec. | "I want to build a feature…", "help me scope…", "write a spec/PRD" |
| **user-stories** | Turns a feature/spec into INVEST user stories with Given/When/Then acceptance criteria. | "write user stories", "acceptance criteria", "break this into tickets" |
| **generate-jira-test-cases** | Pulls a Jira ticket + context, walks you through a six-section QA checklist, and produces a developer-ready test case list. Needs the Atlassian/Jira connector. | "generate test cases for B2-1234", "prepare QA scenarios", "what should we test for this" |

## Install (per PM, one-time)

Skills are installed individually in Claude.

### Claude Desktop / Claude.ai (web)
1. **Download the ready-to-upload zips** — grab them from the [latest Release](../../releases/latest), or from the `dist/` folder in this repo:
   - `feature-brainstorming.zip`
   - `user-stories.zip`
   - `generate-jira-test-cases.zip` *(connect your Atlassian/Jira account when prompted)*
2. In Claude, go to **Settings → Capabilities → Skills** (you need a plan that supports custom Skills) and **upload** each zip.
3. The skills now trigger automatically based on what you ask — or invoke them by name.

> The zips already have `SKILL.md` at their root, so no zipping needed. To update a skill after we change it, just download the new zip and re-upload.

## How a PM uses them

```
Rough idea
   │  (feature-brainstorming)
   ▼
Approved Spec  ──►  share with engineering
   │  (user-stories)
   ▼
User stories + acceptance criteria  ──►  paste into Jira  ──►  ticket gets built
                                                              │  (generate-jira-test-cases)
                                                              ▼
                                                  QA test cases for the developer to verify
```

1. Describe your idea to Claude. `feature-brainstorming` kicks in, asks questions, and produces a spec.
2. Ask Claude to "write user stories from this." `user-stories` produces stories with acceptance criteria and a gap check.
3. Once a ticket exists in Jira, ask "generate test cases for B2-1234." `generate-jira-test-cases` gathers context, walks you through the QA checklist, and outputs a test case list you can post back to the ticket.

## Maintaining (for whoever edits the skills)

After changing any `SKILL.md`, regenerate the upload zips with one command:

```bash
./scripts/build-zips.sh
```

It rebuilds `dist/*.zip` for every folder under `skills/` (so new skills are picked up automatically), with `SKILL.md` at each zip's root. Then commit and, optionally, cut a release:

```bash
git add -A && git commit -m "Update skills" && git push
gh release create v1.1.0 dist/*.zip --title "v1.1.0" --notes "What changed..."
```

## Customizing

The skills are plain Markdown. Edit the `SKILL.md` files to adjust personas, the spec template, or the compliance checklist to match how BrioHR actually works. The `description:` line in each file's frontmatter controls when Claude auto-triggers the skill — keep it specific.

## Contributing (BrioHR PMs)

1. Branch from `main`.
2. Edit the relevant `SKILL.md`.
3. Test it in your own Claude before opening a PR — paste a real feature idea and confirm the behavior.
4. Open a PR describing the real problem the change solves.

## Credit & License

Adapted from [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent (MIT). This repo is MIT licensed — see `LICENSE`.

# BrioHR PM Skills

> **Status:** Live — 3 skills distributed to the PM team via the BrioHR org plugin, auto-syncing on every push.

A small set of [Agent Skills](https://support.anthropic.com/en/articles/skills) for **product managers at BrioHR**, designed to run in **Claude Desktop** and **Claude.ai (web)**. They turn rough product ideas into validated specs and engineering-ready user stories — tailored for HR-software work (multi-country, compliance, roles & permissions, approvals).

These are adapted from the open-source [Superpowers](https://github.com/obra/superpowers) methodology, with all engineering-only machinery (git, shell, sub-agents, hooks) removed so they work in the consumer Claude apps with no terminal.

## What's inside

| Skill | What it does | When it triggers |
|---|---|---|
| **feature-brainstorming** | Socratic discovery — asks one question at a time, proposes 2–3 approaches, then writes a structured spec. Can pull a Jira epic/ticket for context and post the spec back. | "I want to build a feature…", "help me scope…", "write a spec/PRD" |
| **ticket-writing** | Turns a feature/spec/Jira ticket into a single BrioHR-format story (Business Context, Behavior, User Flow, Other Considerations, Given/When/Then Acceptance Criteria), iterates with you, then offers to generate test cases. | "write a ticket", "write a user story", "acceptance criteria", "document this feature" |
| **generate-jira-test-cases** | Pulls a Jira ticket + context, walks you through a six-section QA checklist, and produces a developer-ready test case list. | "generate test cases for B2-1234", "prepare QA scenarios", "what should we test for this" |

> **Connectors:**
> - **Atlassian/Jira** — for ticket context. Required for `generate-jira-test-cases`, optional for the other two.
> - **GitHub** — all three skills read BrioHR's product knowledge from the private **[`BrioHR/knowledge-base`](https://github.com/BrioHR/knowledge-base)** repo (daily auto-scraped source of truth). Connect GitHub in Claude (with access to the BrioHR org) so the skills can ground their output in current documented behavior. They still work without it, just without KB grounding.

## Install

This repo is a **Claude plugin** (Cowork marketplace) — the three skills are bundled and delivered to the BrioHR PM team via Claude's org plugin sync. PMs don't download or upload anything.

### For PMs (the team)
Nothing to do. Once the plugin is provisioned to your group (see admin setup below), the three skills appear automatically in Claude (chat, web, Desktop, Cowork) and **auto-update** whenever a new version is published. Just use them — e.g. "write a ticket for B2-1234".

> Jira: `generate-jira-test-cases` needs the Atlassian/Jira connector; the other two use it optionally. Connect Jira in Claude when prompted.

### Set up a Project (optional, recommended)
A Claude **Project is not created automatically** — you make one yourself in the Claude UI, and it's worth doing if you want the cleaner chat-per-phase workflow.

You can use the skills in any normal chat with no project at all. A project adds two things:
- **Shared project knowledge** across all its chats — drop in BrioHR context, conventions, or a saved spec/ticket once and every chat in the project can use it.
- **Organization** — keep a feature's brainstorm → ticket → test-case chats together.

To set one up (once):
1. In Claude, create a new **Project** (e.g. "PM Work" or one per feature).
2. *(Optional)* Add anything reusable to its **knowledge/files** — e.g. team conventions, or a spec you want the next chat to pick up.
3. Run the skills in chats **inside** that project.

> Heads-up: separate chats in a project don't share each other's *messages* — only the project's knowledge/instructions. So to carry an artifact between chats, **export it as a Markdown file** and upload it to the next chat. See **[One chat vs. chat-per-phase](#one-chat-vs-chat-per-phase)** below.

### For the admin (one-time setup)
An org **owner** connects this private repo and assigns the plugin to the PM group. Full steps are in **[SETUP-ADMIN.md](SETUP-ADMIN.md)**. After that, every push to `main` auto-syncs to the team with no further admin action.

### Fallback: manual zip install
If you ever need a skill outside the plugin, each release also attaches ready-to-upload zips under [Releases](../../releases/latest). Upload a zip in **Settings → Capabilities → Skills** (no extraction needed). Note: the repo is private, so only collaborators can download these.

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

### One chat vs. chat-per-phase

You can run the whole chain two ways:

- **One chat (simplest):** brainstorm → ticket → test cases all in the same conversation. Zero handoff. Best for small features. Trade-off: the chat's context grows, so on long sessions later phases get noisier.
- **A fresh chat per phase (recommended for substantial work):** keeps each phase's context lean and focused, so output stays sharp. At the end of each skill, ask it to **export the artifact as a Markdown file**. Open a **new chat in the same project**, **upload that `.md` file**, and run the next skill. Each artifact (spec → ticket → test cases) is a clean, reviewable checkpoint.

> Why Markdown? In Claude, separate chats don't share each other's history — a *project* shares uploaded knowledge and instructions, not chat messages. Exporting the artifact as a **Markdown file** and uploading it to the next chat is how context travels — and Markdown is re-read most faithfully by the next skill. Carry the **artifact**, not the whole transcript.

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

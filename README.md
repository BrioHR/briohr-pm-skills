# BrioHR PM Skills

> **Status:** Live — 3 skills distributed to the PM team via the BrioHR org plugin, auto-syncing on every push.

A small set of [Agent Skills](https://support.anthropic.com/en/articles/skills) for **product managers at BrioHR**, designed to run in **Claude Desktop** and **Claude.ai (web)**. They turn rough product ideas into validated specs and engineering-ready user stories — tailored for HR-software work (multi-country, compliance, roles & permissions, approvals).

These are adapted from the open-source [Superpowers](https://github.com/obra/superpowers) methodology, with all engineering-only machinery (git, shell, sub-agents, hooks) removed so they work in the consumer Claude apps with no terminal.

## What's inside

| Skill | What it does | When it triggers |
|---|---|---|
| **feature-brainstorming** | Brainstorms a rough idea (Socratic — one question at a time, 2–3 approaches, confirm), then writes it as **one** BrioHR-format ticket (Business Context, Behavior, User Flow, Other Considerations, Given/When/Then Acceptance Criteria). Iterates, then offers to generate test cases. | "brainstorm a feature", "help me scope", "write a ticket", "acceptance criteria", "document this feature" |
| **generate-jira-test-cases** | Pulls a Jira ticket + context, walks you through a six-section QA checklist, and produces a developer-ready test case list. | "generate test cases for B2-1234", "prepare QA scenarios", "what should we test for this" |

> **Connectors:**
> - **Atlassian/Jira** — for ticket context and posting back. Required for `generate-jira-test-cases`, optional for `feature-brainstorming`.
> - **Knowledge base** — no connector needed. The BrioHR Help Center is **bundled inside each skill** (`knowledge-base/`) as a daily-synced snapshot, so grounding works offline — no GitHub attachment and no Cowork Project sync.

## Install

This repo is a **Claude plugin** (Cowork marketplace) — the two skills are bundled and delivered to the BrioHR PM team via Claude's org plugin sync. PMs don't download or upload anything.

### For PMs (the team)
Nothing to do. Once the plugin is provisioned to your group (see admin setup below), the two skills appear automatically in Claude (chat, web, Desktop, Cowork) and **auto-update** whenever a new version is published. Just use them — e.g. "brainstorm a feature" or "generate test cases for B2-1234".

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

> Heads-up: separate chats in a project don't share each other's *messages* — only the project's knowledge/instructions. So to carry an artifact between chats, export it as a file (or save it to project knowledge / the Jira ticket). See **[One chat vs. chat-per-phase](#one-chat-vs-chat-per-phase)** below.

### For the admin (one-time setup)
An org **owner** connects this private repo and assigns the plugin to the PM group. Full steps are in **[SETUP-ADMIN.md](SETUP-ADMIN.md)**. After that, every push to `main` auto-syncs to the team with no further admin action.

### Fallback: manual zip install
If you ever need a skill outside the plugin, each release also attaches ready-to-upload zips under [Releases](../../releases/latest). Upload a zip in **Settings → Capabilities → Skills** (no extraction needed). Note: the repo is private, so only collaborators can download these.

## How a PM uses them

```
Rough idea / feature / Jira ticket
   │  (feature-brainstorming: brainstorm → ticket)
   ▼
BrioHR-format ticket (5 sections)  ──►  paste into Jira  ──►  ticket gets built
   │  (feature-brainstorming offers this once finalized)
   ▼  (generate-jira-test-cases)
QA test cases for the developer to verify
```

1. Describe your idea to Claude. `feature-brainstorming` asks questions, proposes 2–3 approaches, then writes it up as one BrioHR-format ticket and iterates with you.
2. Once the ticket's finalized, `generate-jira-test-cases` gathers context, walks you through the six-section QA checklist, and outputs a test case list you can post back to the ticket.

### Use either skill on its own

The two skills are **independent — use one or both, in any order.** Each only activates when your request matches it:

- "Brainstorm a feature" / "write a ticket for this idea" → **feature-brainstorming**
- "Generate test cases for B2-1234" → **generate-jira-test-cases**

The chain is opt-in: `feature-brainstorming` *offers* to hand off to `generate-jira-test-cases`. Say no and it stops. A PM who already has a ticket can jump straight to `generate-jira-test-cases`.

### One chat vs. chat-per-phase

You can run the chain two ways:

- **One chat (simplest):** brainstorm → ticket → test cases all in the same conversation. Zero handoff. Best for small features. Trade-off: the chat's context grows.
- **A fresh chat per phase (leaner context):** at the end of `feature-brainstorming`, ask it to **export the ticket as a Markdown file**. Open a **new chat in the same project**, **upload the `.md`**, and run `generate-jira-test-cases`.

> Why a file? In Claude, separate chats don't share each other's history — a *project* shares uploaded knowledge and instructions, not chat messages. Exporting the ticket as a Markdown file (or posting it to the Jira ticket) is how it travels between chats. Carry the **artifact**, not the transcript.

## Maintaining (for whoever edits the skills)

**Releases are automatic.** Every push to `main` triggers a GitHub Action
(`.github/workflows/release.yml`) that rebuilds the zips and publishes a new
release. The version bump depends on what changed since the last release:

- **Skill or tooling changes → minor bump** (`1.26.0 → 1.27.0`).
- **A knowledge-base sync only → patch bump** (`1.27.0 → 1.27.1`), done
  automatically by the KB sync (see below) — no human action.

So the only maintenance step for a skill change is:

```bash
git add -A && git commit -m "What changed" && git push
```

Within a minute, a new release with fresh zips appears at
[`/releases/latest`](../../releases/latest), and the plugin auto-syncs to the team.

**To preview the zips locally before pushing** (the same ones the Action will build):

```bash
./scripts/build-zips.sh   # writes dist/*.zip (git-ignored)
```

The build script auto-discovers every folder under `skills/`, so new skills are
picked up automatically with no config. Each zip includes that skill's bundled
`knowledge-base/`, so it's a few MB and self-contained.

### Knowledge base (bundled & auto-scraped)

Each skill carries a snapshot of the BrioHR Help Center under
`skills/<skill>/knowledge-base/`, so grounding works offline with no connector —
**don't edit it by hand.**

`.github/workflows/kb-sync.yml` runs daily: it re-scrapes the Help Center with
`scripts/kb/scraper.py`, vendors the result into every skill's `knowledge-base/`,
and — if any article or the catalog changed — commits, bumps the **patch**
version, and cuts a release, so PMs auto-update. **No token or secret needed:**
the Help Center is public and the job pushes with the built-in `GITHUB_TOKEN`.

> The scraper is a pristine copy of the one in
> [`BrioHR/knowledge-base`](https://github.com/BrioHR/knowledge-base) — keep the two
> in step so both mirror the same source.

## Customizing

The skills are plain Markdown. Edit the `SKILL.md` files to adjust personas, the spec template, or the compliance checklist to match how BrioHR actually works. The `description:` line in each file's frontmatter controls when Claude auto-triggers the skill — keep it specific.

## Contributing (BrioHR PMs)

1. Branch from `main`.
2. Edit the relevant `SKILL.md`.
3. Test it in your own Claude before opening a PR — paste a real feature idea and confirm the behavior.
4. Open a PR describing the real problem the change solves.

## Credit & License

Adapted from [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent (MIT). This repo is MIT licensed — see `LICENSE`.

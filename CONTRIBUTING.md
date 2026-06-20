# Contributing to BrioHR PM Skills

This repo holds the BrioHR PM skills for Claude (Desktop / Claude.ai). Anyone on the product team can improve a skill. You don't need release or versioning knowledge — that's automatic.

## One-time setup

1. Accept the repo invite (you'll get an email, or it's under your GitHub notifications).
2. Have **Claude Code** installed and signed in to your own GitHub account.
3. Clone the repo:
   ```bash
   git clone https://github.com/product-briohr/briohr-pm-skills.git
   cd briohr-pm-skills
   ```

## The edit → test → ship loop

1. **Edit a skill.** Each skill is a folder under `skills/` with a `SKILL.md`. Open it in Claude Code and describe what you want to change (e.g. "add a permissions check to the ticket-writing skill").

2. **Test before you push** — two easy ways:
   - **Fastest:** ask Claude in the same session to *run* the skill on a real example (e.g. "run ticket-writing on B2-6726") and read the output.
   - **Real install:** build the upload zips locally and try one in your own Claude Desktop:
     ```bash
     ./scripts/build-zips.sh   # writes dist/*.zip (git-ignored)
     ```
     Upload a zip via **Settings → Capabilities → Skills**.

3. **Ship it.** Commit and push to `main`:
   ```bash
   git add -A
   git commit -m "Short description of what you changed"
   git push
   ```

That's it. Within seconds, automatically:
- the version bumps (`v1.0 → v1.1 → v1.2 …`),
- fresh zips are attached to a new [release](../../releases/latest),
- **#product-hotline** gets a Slack ping with the version, your name, and your commit message as the changelog.

## Tips

- **Write a clear commit message** — it becomes the changelog line in the Slack notification. "Add timezone edge case to test cases" is good; "update" is not.
- **One change per push** when you can — keeps each version's changelog meaningful.
- **Don't commit secrets.** The repo is public. The Slack webhook lives in a GitHub Actions secret, not in the code.
- **The `description:` line** in each `SKILL.md` frontmatter controls when Claude auto-triggers that skill. Keep it specific if you edit it.

## Questions

Drop them in **#product-hotline**.

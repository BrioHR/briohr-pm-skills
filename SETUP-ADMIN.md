# Admin Setup — one-time (org owner only)

This connects the BrioHR PM Skills plugin to your Claude org and gives it to the PM team, so they get the skills automatically and receive every future update with no action. You only do this **once**.

> Requires: a Claude **Team or Enterprise** plan, and you must be an **Owner / Primary Owner** (only owners can manage org plugins).

## Steps

### 1. Connect this repo as a plugin source
1. Go to **Organization settings → Plugins**.
2. Choose **Connect a GitHub repository**.
3. When prompted to sign in to GitHub, use an account with access to the **BrioHR** org, and select **`BrioHR/briohr-pm-skills`**. Approve access.
4. Turn on **Sync automatically**.

### 2. Assign the plugin to the PM group
1. Still under **Organization settings → Plugins**, find **`briohr-pm-skills`**.
2. In the **Custom access** column, click **Add groups**.
3. Select your **Product / PM group** (create the group first under member/group settings if it doesn't exist).
4. Set the install preference to **Required** (the team gets it automatically and can't turn it off — it stays on for everyone in the group).

### 3. Done
The 4 PMs now see the two skills in Claude (chat, web, Desktop, and Cowork) automatically. Group targeting set up for Cowork carries over to chat with no extra steps.

### 4. Enable the daily knowledge-base sync (one-time repo secret)
The skills ground their output in a snapshot of the **`BrioHR/knowledge-base`** repo that is **bundled inside each skill**, so PMs get grounding automatically — no Cowork Project sync, no GitHub attachment, no connector. A GitHub Action keeps that bundled snapshot fresh daily; it just needs read access to the private KB repo via one repo secret.

1. Get a token with **read access to `BrioHR/knowledge-base`** — either the org **Claude GitHub App** installation token, or a **fine-grained PAT** (Repository access: `BrioHR/knowledge-base`, Contents: Read-only).
2. In **`BrioHR/briohr-pm-skills` → Settings → Secrets and variables → Actions**, add a repository secret named **`KB_SYNC_TOKEN`** set to that token.
3. Done. `.github/workflows/kb-sync.yml` then runs daily (and on manual dispatch), pulls any KB changes into the skills, and pushes to `main` — which auto-publishes a **patch** release to the team.

Without `KB_SYNC_TOKEN` the skills still work with the KB snapshot committed at build time; it just won't refresh automatically.

## How updates work after setup
- A PM (or whoever maintains the skills) pushes a change to `main`.
- The repo's GitHub Action bumps the plugin version (minor) and the marketplace auto-syncs.
- The PM group **automatically gets the new version** — no reinstall, no admin action.
- A summary is posted to **#product-hotline** for visibility.
- Separately, the knowledge base re-syncs daily; any change ships as a **patch** release the same way, with no human action.

## Notes
- The repo is **private** (required for GitHub plugin sync). Keep it private.
- Group-level access overrides persist across re-syncs, so you won't need to reassign the group on updates.
- To add a new PM later: just add them to the PM group — they inherit the plugin automatically.

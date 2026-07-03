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

### 4. Enable knowledge-base grounding (separate from the plugin install)
The skills ground their output in the private **`BrioHR/knowledge-base`** repo. This needs the **Claude GitHub App installed on the `BrioHR` organization** — a separate installation from any personal-account one, since "All repositories" only covers repos owned by *that installation's* account.

1. Go to **github.com/organizations/BrioHR/settings/installations**.
2. Find the **Claude** GitHub App. If it isn't listed, install/authorize it for the org.
3. Open it → **Repository access** → make sure it includes `BrioHR/knowledge-base` (either "All repositories" or explicitly selected).
4. PMs then get KB grounding by **syncing the repo into their Cowork Project** (or attaching an article via **+ → Add from GitHub** in plain chat). Without this, the skills still work — just without KB grounding.

## How updates work after setup
- A PM (or whoever maintains the skills) pushes a change to `main`.
- The repo's GitHub Action bumps the plugin version and the marketplace auto-syncs.
- The PM group **automatically gets the new version** — no reinstall, no admin action.
- A summary is posted to **#product-hotline** for visibility.

## Notes
- The repo is **private** (required for GitHub plugin sync). Keep it private.
- Group-level access overrides persist across re-syncs, so you won't need to reassign the group on updates.
- To add a new PM later: just add them to the PM group — they inherit the plugin automatically.

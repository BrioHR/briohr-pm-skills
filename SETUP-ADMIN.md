# Admin Setup — one-time (org owner only)

This connects the BrioHR PM Skills plugin to your Claude org and gives it to the PM team, so they get the skills automatically and receive every future update with no action. You only do this **once**.

> Requires: a Claude **Team or Enterprise** plan, and you must be an **Owner / Primary Owner** (only owners can manage org plugins).

## Steps

### 1. Connect this repo as a plugin source
1. Go to **Organization settings → Plugins**.
2. Choose **Connect a GitHub repository**.
3. Sign in with the GitHub account Amir gives you, and select **`product-briohr/briohr-pm-skills`**.
4. Turn on **Sync automatically**.

> If you hit an "owner needs to approve" prompt, just tell Amir — he approves it once and you continue.

### 2. Assign the plugin to the PM group
1. Still under **Organization settings → Plugins**, find **`briohr-pm-skills`**.
2. In the **Custom access** column, click **Add groups**.
3. Select your **Product / PM group** (create the group first under member/group settings if it doesn't exist).
4. Set the install preference to **Installed by default** (so the team gets it automatically; you can use *Required* if you want it non-removable).

### 3. Done
The 4 PMs now see the three skills in Claude (chat, web, Desktop, and Cowork) automatically. Group targeting set up for Cowork carries over to chat with no extra steps.

## How updates work after setup
- A PM (or whoever maintains the skills) pushes a change to `main`.
- The repo's GitHub Action bumps the plugin version and the marketplace auto-syncs.
- The PM group **automatically gets the new version** — no reinstall, no admin action.
- A summary is posted to **#product-hotline** for visibility.

## Notes
- The repo is **private** (required for GitHub plugin sync). Keep it private.
- Group-level access overrides persist across re-syncs, so you won't need to reassign the group on updates.
- To add a new PM later: just add them to the PM group — they inherit the plugin automatically.

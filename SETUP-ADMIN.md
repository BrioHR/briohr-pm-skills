# Admin Setup — one-time (org owner only)

This connects the BrioHR PM Skills plugin to your Claude org and gives it to the PM team, so they get the skills automatically and receive every future update with no action. You only do this **once**.

> Requires: a Claude **Team or Enterprise** plan, and you must be an **Owner / Primary Owner** (only owners can manage org plugins).

## Steps

### 1. Connect this repo as a plugin source

> **Which GitHub account?** You connect with **your own personal GitHub account — not the `product-briohr` login.** Claude verifies your personal token only to confirm you have access, then Cowork's GitHub App does the actual syncing. Two prerequisites:
> - Your GitHub account must be a **collaborator** on `product-briohr/briohr-pm-skills` (read access is enough). Ask the repo owner to add you.
> - Because the repo is owned by a personal account, the **repo owner (`product-briohr`) approves the Cowork GitHub App** the first time. If you see an "owner must approve" prompt, that's expected — it routes to them for a one-time click.

1. Go to **Organization settings → Plugins**.
2. Choose **Connect a GitHub repository** (Cowork syncs plugins from it).
3. Sign in with **your own GitHub account** and select the private repo **`product-briohr/briohr-pm-skills`**.
4. If prompted, have the repo owner approve the Cowork GitHub App's access (one-time).
5. Turn on **Sync automatically** — the marketplace then re-syncs whenever changes land on `main`.

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

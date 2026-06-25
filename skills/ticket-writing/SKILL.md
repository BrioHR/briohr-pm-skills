---
name: ticket-writing
description: "Use to turn a feature, spec, or Jira ticket into a single well-formed BrioHR ticket/user story, written in BrioHR's standard format: Business Context, Behavior, User Flow, Other Considerations, and Given/When/Then Acceptance Criteria. Triggers when a PM says 'write a ticket', 'write a user story', 'write the acceptance criteria', 'draft this ticket', 'document this feature', or pastes a feature/ticket and wants it written up for engineering. Tailored for BrioHR HR-software personas."
---

# Ticket Writing (User Story & Acceptance Criteria)

Turn a feature, spec, or Jira ticket into **one** clear, complete user story written in BrioHR's standard story format. The story is documented with exactly five sections — **Business Context, Behavior, User Flow, Other Considerations, Acceptance Criteria** — matching how BrioHR Jira tickets (e.g. `B2-####` Stories) are written.

**Output is a single story in these five sections — nothing else.** Do NOT add a story-map table, do NOT split the feature into multiple stories, and do NOT append a separate "gap check." If something is undecided, capture it inside **Other Considerations** as an open point. If the input genuinely describes several unrelated features, say so and ask the PM which one to write — don't auto-decompose.

## BrioHR Product Context

BrioHR is an HR SaaS platform serving ASEAN markets, primarily **Malaysia and Singapore**. Ground stories and acceptance criteria in this — not generic SaaS.

**Modules:** Profile/Personal Info, Claims, Leaves, Payroll (Malaysia), Payroll (Singapore), Time Attendance, Document Management, Onboarding, Recruitment, Training.

**Platforms (call out which a story applies to):** Web (primary — admin config, settings, reporting), Mobile (employee requests & approvals only; Android 5.1+, iOS 14.0+, Huawei HMS build), Superadmin (BrioHR-internal per-tenant feature toggles). Never put admin-only steps in a Mobile story.

**Default personas → typical module rights:**
- **Employee** — self-service: own profile, submit leave/claims, view payslip (mostly Mobile + Web).
- **Line Manager** — approve/reject team requests, view team data.
- **HR Admin** — configure modules, manage employees, run payroll, reporting (Web).
- **Payroll Officer** — payroll cycles, statutory contributions, bank/IRAS files.
- **Recruiter** — recruitment pipeline, offers, hand-off to Onboarding.
- **Executive / Reporting viewer** — dashboards and exports.

**Statutory edge cases to cover when payroll/leave/attendance is involved:**
- Malaysia: EPF, SOCSO, EIS, PCB (MTD), Zakat, HRDF; mid-month joiners/leavers, proration, OT, unpaid leave effects.
- Singapore: CPF (OW/AW caps), SHG funds, SDL, IRAS (IR8A/AIS); PR vs Citizen vs EP/DP differences.

**Salary test data ranges (use in acceptance criteria for payroll stories):**
- Malaysia: MYR 1,500 / 5,000 / 15,000 / 40,000 (low → very high).
- Singapore: SGD 2,000 / 6,000 / 12,000 / 30,000 (low → very high).

**Cross-module ripple patterns:** Profile/Leave/Onboarding → many modules; Attendance & Leave → Payroll; Claims → Payroll (reimbursement with salary); Recruitment → Onboarding → Profile.

## BrioHR Knowledge Base (single source of truth)

To ground the ticket in current documented behavior, consult the **`BrioHR/knowledge-base`** GitHub repo — the daily-updated source of truth (auto-scraped from the Help Center). **Do NOT fetch the support website (`support.briohr.com`) anymore.**

Access it via the **GitHub connector** (connect GitHub in Claude if prompted):
- Start with **`INDEX.md`** or **`sitemap.json`** to find the relevant **category → subcategory** for the module.
- Open the matching article `.md` file(s) under `<category>/<subcategory>/` for documented behavior, settings, and permissions — so the Behavior, User Flow, and Acceptance Criteria match reality.

If the GitHub connector isn't available, say so once and continue from the PM's input — don't scrape the website.

## Jira Context (optional — uses the Atlassian connector)

The source for stories is often a Jira epic/ticket. If the PM gives a `B2-####` key, a `briohr.atlassian.net` URL, or asks to "write stories for this epic," use the Jira tools:
- **Read the epic/ticket** — title, description, comments, linked items, and existing subtasks. Don't write a story that duplicates a subtask that already exists.
- **Search sibling tickets** in the same module for prior decisions and edge cases:
  `project = B2 AND summary ~ "<distinctive keyword>" ORDER BY updated DESC`.
- Treat the ticket as the source of truth for scope; still ask 1–3 clarifying questions if it's ambiguous.

If the connector isn't available, say so once and work from whatever the PM pasted.

**After presenting the story**, offer (don't force):
> "Want me to post this story as a comment on the ticket, or update the ticket description with it?"
Only write to Jira if the PM says yes; then share the link.

## Before you write anything

1. **Get the source.** A Jira ticket (see above), a feature/spec, or the brainstorming spec doc. If it's vague, ask 1–3 clarifying questions first — do NOT invent requirements.
2. **Identify the personas involved.** Default BrioHR personas: **Employee**, **Line Manager**, **HR Admin**, **Payroll Officer**, **Recruiter**, **Executive/Reporting viewer**. A single story usually centers on one primary persona but may describe how others (e.g. a reviewing manager) interact — capture that in Behavior and User Flow.
3. **Confirm scope.** What's in this version vs. later. State anything deferred inside **Other Considerations** (out of scope), don't silently drop it.

## Output format

Produce **one** story in this **exact** five-section shape, in this order. This is the entire output — no table before it, no gap check after it.

```markdown
# [Story title]
**Module:** [e.g. Time Attendance]   **Platform(s):** [Web / Mobile / Superadmin]

## Business Context
Why this feature matters — the goals, the value to the user or business, and any
constraints driving it. Answer "why are we building this?" (not what it does).

## Behavior
A high-level description of what the feature does from the user's perspective —
what they can now do and what the system does in response. Not implementation.

## User Flow
The step-by-step sequence of user actions / screens to accomplish the goal.
Split by persona if more than one is involved (e.g. Employee Flow, Manager Flow):
1. User does X (on [screen/platform])
2. System responds with Y
3. User does Z
…

## Other Considerations
Any extra notes: technical constraints, dependencies, non-functional requirements
(performance, security), edge cases, accessibility, data rules (effective dating,
audit trail), explicit out-of-scope items, and any open/undecided points.

## Acceptance Criteria
The definition of done — specific, testable conditions. Use Given/When/Then:
- **Given** [context] **When** [action] **Then** [observable result]
- **Given** … **When** … **Then** …
```

Every section is required. If a section genuinely has nothing, write a short "None" rather than deleting the heading.

## Rules for a good story

- **Business Context explains *why*, not *what*.** Don't repeat the Behavior here — state the goal/value/constraint.
- **Behavior is from the user's perspective.** Describe observable behavior, not database tables or API design.
- **User Flow is concrete and numbered.** Name the actual screens/platforms and split by persona when more than one acts; don't write "user uses the feature."
- **Other Considerations is where edge cases, dependencies, and open questions live** — don't drop them, and don't spin them into separate stories.
- **Acceptance Criteria are testable.** Every Then must be observable. No "works correctly" or "is fast" — state the actual expected behavior or threshold. Include unhappy paths: validation errors, empty/zero state, permission denied, and the most likely failure.

## HR-specific details to weave in (where relevant)

These belong inside **Behavior**, **User Flow**, **Other Considerations**, or **Acceptance Criteria** of the single story — not as separate stories:
- **Permissions** — each persona's view/create/edit/approve rights.
- **Approval workflow** — submit, approve, reject (with reason), and what each party sees.
- **Multi-country / multi-entity** — does behavior differ by country, currency, or legal entity?
- **Effective dating & audit trail** — historical values, "as-of" dates, who-changed-what.
- **Joiners / leavers / part-time** — proration, mid-cycle changes, deactivated users.
- **Notifications** — who gets emailed/notified and when.
- **Reporting / export** — filterable and exportable (CSV/Excel/PDF)?
- **Data privacy** — sensitive fields, masking, PDPA/GDPR.

## Self-review before handing over

- Are all five sections present and filled (Business Context, Behavior, User Flow, Other Considerations, Acceptance Criteria)?
- Does Business Context explain *why* (not just restate the Behavior)?
- Is the User Flow concrete and numbered, with real screens/platforms?
- Does every acceptance criterion have an observable Then?
- Did you include unhappy-path criteria (validation, permissions, empty state)?
- Are edge cases and out-of-scope items captured in Other Considerations, not dropped?
- Did you avoid adding a story map, multiple stories, or a separate gap-check section?

## After presenting the story — iterate, then hand off

Run these two steps in order. Do not skip straight to test cases.

**Step 1 — Ask if anything is missing.** After presenting the story, ask:
> "Want to add or change anything — extra edge cases, another persona's flow, more acceptance criteria, or adjust any section?"

If the PM gives input, fold it into the relevant section(s), re-present the updated story, and ask again. Repeat until the PM says it's finalized.

**Step 2 — Finalize & hand off (to skill 3).** Once the PM confirms the story is finalized, offer how to continue:
> "Story's finalized. Want me to generate the QA test cases now (here in this chat), or **export the ticket as a Markdown file** so you can continue in a fresh chat?"

- **Export for a fresh chat (leaner context):** generate the ticket as a downloadable **Markdown (`.md`) file** — Markdown because the next skill re-reads it most faithfully. Make sure it contains the complete 5-section ticket. Tell the PM to open a **new chat in the same project**, upload the `.md` file, and say *"Generate test cases from this ticket."*
- **Same chat:** invoke the **`generate-jira-test-cases`** skill, passing this finalized ticket. That skill walks them through the six-section QA checklist and produces the developer-ready test case list.
- If the PM declines test cases, stop here.

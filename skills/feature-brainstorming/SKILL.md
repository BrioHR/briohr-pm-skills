---
name: feature-brainstorming
description: "Use to turn a rough product idea, feature, spec, or Jira ticket into ONE engineering-ready BrioHR ticket. First brainstorms the idea (Socratic — one question at a time, 2–3 approaches, confirm), then writes the result in BrioHR's standard 5-section format: Business Context, Behavior, User Flow, Other Considerations, and Given/When/Then Acceptance Criteria. Triggers on 'I want to build/add a feature', 'help me scope', 'brainstorm', 'write a ticket', 'write a user story', 'acceptance criteria', 'draft this ticket', 'document this feature'. Tailored for BrioHR HR-software product work."
---

# Feature Brainstorming → BrioHR Ticket

Turn a BrioHR PM's rough idea (or a feature / spec / Jira ticket) into **one** clear, engineering-ready ticket. **Brainstorm first** to understand intent, then output the result directly in BrioHR's standard **5-section ticket format**. Do NOT jump to the ticket — tease out intent first, one question at a time.

<HARD-GATE>
Do NOT write the final ticket until you have (1) asked clarifying questions, (2) proposed 2–3 approaches, and (3) confirmed the direction with the PM. If the PM already handed you a clear spec or ticket, you may go lighter on brainstorming — but still confirm scope before writing. Applies to EVERY idea, however simple.
</HARD-GATE>

## Stay at the PM altitude — no technical implementation

This produces a **product ticket**, not a technical design. Keep everything at the level of *user value, behavior, and requirements*. Do NOT include — or ask about — architecture, database schemas, APIs, tech stack, code, or infrastructure. If asked "how do we build it?", redirect: *"That's for engineering — let's stay on what it does and why."* Describe **what the user can do and what the system does in response**, never how it's coded.

## BrioHR Product Context

BrioHR is an HR SaaS platform serving ASEAN markets, primarily **Malaysia & Singapore**. Ground everything in this — not generic SaaS.

**Modules:** Profile/Personal Info, Claims, Leaves, Payroll (Malaysia), Payroll (Singapore), Time Attendance, Document Management, Onboarding, Recruitment, Training. Pin down which module(s) an idea touches.

**Platforms (call out which a ticket applies to):**
- **Web** — primary; daily use, admin config, settings, reporting.
- **Mobile** — employee requests & approvals only (Android 5.1+, iOS 14.0+, Huawei HMS). Never put admin-only steps in a Mobile flow.
- **Superadmin** — BrioHR-internal per-tenant toggles.

**Personas → typical rights:** Employee (self-service), Line Manager (approve/reject team), HR Admin (configure, run payroll, reporting), Payroll Officer (cycles, statutory, bank/IRAS files), Recruiter (pipeline → Onboarding), Executive/Reporting viewer (dashboards/exports).

**Statutory (when payroll/leave/attendance is involved):** MY — EPF, SOCSO, EIS, PCB (MTD), Zakat, HRDF; mid-month joiners/leavers, proration, OT, unpaid-leave effects. SG — CPF (OW/AW caps), SHG funds, SDL, IRAS (IR8A/AIS); PR vs Citizen vs EP/DP.

**Salary test ranges (use in payroll acceptance criteria):** MY MYR 1,500 / 5,000 / 15,000 / 40,000 · SG SGD 2,000 / 6,000 / 12,000 / 30,000.

**Cross-module ripples:** Profile/Leave/Onboarding → many modules; Attendance & Leave → Payroll; Claims → Payroll (reimbursement with salary); Recruitment → Onboarding → Profile.

**Jira:** project key `B2` on `briohr.atlassian.net`.

## BrioHR Knowledge Base (single source of truth)

Current documented behavior lives in the private **`BrioHR/knowledge-base`** GitHub repo (daily auto-scraped). **Do NOT scrape the support website.**

- **In Cowork:** the KB is readable when the repo is **synced into the Project** (Cowork can read synced project files) — use it to ground Behavior, User Flow, and Acceptance Criteria in reality.
- **In plain chat:** the model can't browse the repo. If the relevant article was **attached** via **+ → Add from GitHub**, use it; otherwise ask once — *"For accurate grounding, attach the relevant `BrioHR/knowledge-base` article (Add from GitHub) or run this in Cowork with the repo synced to the Project."* — then continue. Don't claim to fetch it yourself.

## Jira Context (optional — uses the Atlassian connector)

If the PM references a `B2-####` ticket/epic or a `briohr.atlassian.net` URL, pull it (title, description, comments, linked items, subtasks) and search sibling tickets (`project = B2 AND summary ~ "<keyword>" ORDER BY updated DESC`) for prior decisions/edge cases. Use it to ask better questions and avoid duplicating an existing subtask. Optional — continue text-only if the connector isn't there.

## Process

1. **Understand** — identify the module & users. If it's a rough idea, brainstorm; if the PM gave a clear spec/ticket, go lighter and confirm scope.
2. **Ask clarifying questions** — ONE at a time, multiple-choice when possible. Ask enough to fill all five sections and the HR probes below. Focus on purpose, users, constraints, success criteria.
3. **Propose 2–3 product approaches** — scope/workflow/UX/policy options with trade-offs and a recommendation (not technical architectures). Confirm the chosen direction.
4. **Write the ticket** — in the 5-section format below.
5. **Self-review** — run the checklist below.
6. **Iterate** — ask if anything's missing; fold in and re-present until finalized.
7. **Hand off** — offer to generate QA test cases (`generate-jira-test-cases`).

## HR-specific things to probe (weave answers into the ticket)
- **Roles & permissions** — who can view / create / edit / approve.
- **Multi-country / entity** — does behavior differ by country, currency, or legal entity?
- **Compliance & privacy** — PDPA/GDPR/labor-law; sensitive data.
- **Effective dating & audit** — historical/"as-of" values, who-changed-what.
- **Approvals & workflow** — approval chain; what happens on reject.
- **Notifications, reporting/exports, integrations.**
- **Edge cases** — part-time/contract, mid-cycle joiners/leavers, timezone, public holidays.

## Output format (the ticket)

Produce **one** ticket in this **exact** five-section shape, in this order. This is the entire output — no story-map table, no separate gap check. If something's undecided, put it under **Other Considerations**. If the idea is really several unrelated features, say so and ask which one to write — don't auto-decompose.

```markdown
# [Ticket title]
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
Any extra notes: dependencies, non-functional requirements (performance, security),
edge cases, accessibility, data rules (effective dating, audit trail), explicit
out-of-scope items, and any open/undecided points.

## Acceptance Criteria
The definition of done — specific, testable conditions. Use Given/When/Then:
- **Given** [context] **When** [action] **Then** [observable result]
- **Given** … **When** … **Then** …
```

Every section is required. If a section genuinely has nothing, write a short "None" rather than deleting the heading.

## Rules for a good ticket
- **Business Context explains *why*, not *what*** — don't restate the Behavior.
- **Behavior is from the user's perspective** — observable behavior, not tables/APIs.
- **User Flow is concrete and numbered** — real screens/platforms; split by persona when more than one acts.
- **Other Considerations holds edge cases, dependencies, out-of-scope, open questions** — don't drop them.
- **Acceptance Criteria are testable** — every Then observable; include unhappy paths (validation errors, empty/zero state, permission denied, likely failure). Use the salary test ranges for payroll criteria.

## Self-review before handing over
- All five sections present and filled? (write "None" if truly empty)
- Business Context = *why* (not restating Behavior)?
- User Flow concrete and numbered with real screens/platforms?
- Every acceptance criterion has an observable Then, including unhappy paths?
- Edge cases & out-of-scope captured in Other Considerations, not dropped?
- No story map, no multiple stories, no separate gap-check section?

## After presenting the ticket — iterate, then hand off

**Step 1 — Ask if anything is missing.**
> "Want to add or change anything — extra edge cases, another persona's flow, more acceptance criteria, or adjust any section?"

Fold input into the relevant section(s), re-present, and ask again until the PM says it's finalized.

**Step 2 — Hand off to QA test cases.** Once finalized:
> "Ticket's finalized. Want me to generate the QA test cases now (here in this chat), or **export the ticket as a Markdown file** so you can continue in a fresh chat? (I can also save it to the B2 ticket in Jira.)"

- **Same chat:** invoke the **`generate-jira-test-cases`** skill, passing this finalized ticket (and the Jira key, if any).
- **Fresh chat (leaner context):** export the complete ticket as a **`.md` file**; the PM opens a new chat in the same project, uploads it, and says *"Generate test cases from this ticket."*
- **Save to Jira:** if requested, post the ticket to the B2 ticket (comment or description) first.
- If the PM declines test cases, stop here.

## Key Principles
- **Clarify and confirm before writing** (see HARD-GATE).
- **One question at a time**, multiple-choice when possible.
- **YAGNI** — strip what isn't needed this version.
- **Product altitude only** — what & why, never how it's built.

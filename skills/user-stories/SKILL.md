---
name: user-stories
description: "Use to turn a feature, spec, or Jira epic into well-formed BrioHR user stories. Each story is documented with Business Context, Behavior, User Flow, Other Considerations, and Given/When/Then Acceptance Criteria. Triggers when a PM says 'write user stories', 'acceptance criteria', 'break this into stories', 'tickets for eng', or pastes a spec/feature/epic and wants it decomposed for engineering. Tailored for BrioHR HR-software personas."
---

# User Stories & Acceptance Criteria

Turn a feature or spec into a set of clear, independent user stories that an engineer with no product context could pick up and build. Each story is documented with five sections — **Business Context, Behavior, User Flow, Other Considerations, Acceptance Criteria** — so the reader understands not just *what* to build but *why* and *how* it's used.

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

## Jira Context (optional — uses the Atlassian connector)

The source for stories is often a Jira epic/ticket. If the PM gives a `B2-####` key, a `briohr.atlassian.net` URL, or asks to "write stories for this epic," use the Jira tools:
- **Read the epic/ticket** — title, description, comments, linked items, and existing subtasks. Don't write a story that duplicates a subtask that already exists.
- **Search sibling tickets** in the same module for prior decisions and edge cases:
  `project = B2 AND summary ~ "<distinctive keyword>" ORDER BY updated DESC`.
- Treat the ticket as the source of truth for scope; still ask 1–3 clarifying questions if it's ambiguous.

If the connector isn't available, say so once and work from whatever the PM pasted.

**After presenting the stories**, offer (don't force):
> "Want me to add these as subtasks under the epic, or post them as a comment on the ticket?"
Only write to Jira if the PM says yes; then share the link(s).

## Before you write anything

1. **Get the source.** A Jira epic/ticket (see above), a feature/spec, or the brainstorming spec doc. If it's vague, ask 1–3 clarifying questions first — do NOT invent requirements.
2. **Confirm the personas.** Default BrioHR personas: **Employee**, **Line Manager**, **HR Admin**, **Payroll Officer**, **Recruiter**, **Executive/Reporting viewer**. Confirm which apply.
3. **Confirm scope.** What's in this version vs. later (YAGNI). Don't write stories for out-of-scope behavior.

## Story format

Each story uses this **exact** five-section shape, in this order:

```markdown
### [Short story title]
**Persona:** [Employee / Line Manager / HR Admin / Payroll Officer / Recruiter / Executive]   **Platform:** [Web / Mobile / Superadmin]

**Business Context**
Why this story matters — the goal, the value to the user or business, and any
constraints driving it. 1–3 sentences. Answer "why are we building this?"

**Behavior**
A high-level description of what the feature does from the user's perspective —
what they can now do and what the system does in response. Not implementation.

**User Flow**
The step-by-step sequence of user actions / screens to accomplish the goal:
1. User does X (on [screen/platform])
2. System responds with Y
3. User does Z
…

**Other Considerations**
Extra notes that aren't the happy path: technical constraints, dependencies on
other stories or modules, non-functional requirements (performance, security),
edge cases, accessibility, data rules (effective dating, audit trail), and
explicit out-of-scope items.

**Acceptance Criteria**
The definition of done — specific, testable conditions. Use Given/When/Then:
- **Given** [context] **When** [action] **Then** [observable result]
- **Given** … **When** … **Then** …
```

Every section is required. If a section genuinely has nothing (e.g., no special "Other Considerations"), write a short "None" rather than deleting the heading — consistency helps readers and Jira import.

## Rules for good stories

- **One capability per story.** If the **Behavior** describes two distinct capabilities joined by "and," split it into two stories.
- **INVEST:** each story should be Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Vertical slices, not layers.** A story delivers user-visible value end-to-end — never "build the database table" as its own story.
- **Business Context explains *why*, not *what*.** Don't repeat the Behavior here — state the goal/value/constraint.
- **User Flow is concrete and numbered.** Name the actual screens/platforms; don't write "user uses the feature."
- **Acceptance Criteria are testable.** Every Then must be observable. No "works correctly" or "is fast" — state the actual expected behavior or threshold.
- **Cover the unhappy paths in Acceptance Criteria.** For each story add criteria for: validation errors, empty/zero state, permission denied, and the most likely failure.

## HR-specific coverage to always consider

For each feature, check whether you need stories or criteria for:
- **Permissions matrix** — each persona's view/create/edit/approve rights (usually its own story).
- **Approval workflow** — submit, approve, reject (with reason), and what each party sees.
- **Multi-country / multi-entity** — does behavior differ by country, currency, or legal entity?
- **Effective dating & audit trail** — historical values, "as-of" dates, who-changed-what.
- **Joiners / leavers / part-time** — proration, mid-cycle changes, deactivated users.
- **Notifications** — who gets emailed/notified and when.
- **Reporting / export** — can the data be filtered and exported (CSV/PDF)?
- **Data privacy** — sensitive fields, masking, PDPA/GDPR access & deletion.

## Output structure

Produce, in this order:

1. **Story map / summary table** — a list of the stories with persona and a one-line description, so the PM can see coverage at a glance.
2. **The full stories** — each with all five sections (Business Context, Behavior, User Flow, Other Considerations, Acceptance Criteria), grouped by persona or by flow.
3. **Gap check** — a short "Did we miss anything?" section calling out personas, edge cases, or compliance items that have no story yet, so the PM can decide whether to add them.

## Self-review before handing over

- Does every story have all five sections filled (Business Context, Behavior, User Flow, Other Considerations, Acceptance Criteria)?
- Does Business Context explain *why* (not just restate the Behavior)?
- Is the User Flow concrete and numbered, with real screens/platforms?
- Does every acceptance criterion have an observable Then?
- Is every persona from scope covered by at least one story?
- Did you include unhappy-path criteria (validation, permissions, empty state)?
- Are any stories actually two stories? Split them.
- Are out-of-scope items explicitly listed (in Other Considerations), not silently dropped?

Then offer:
> "Here are the stories. Want me to add them as subtasks under the epic, post them as a comment, tighten any story, or add edge-case coverage?"

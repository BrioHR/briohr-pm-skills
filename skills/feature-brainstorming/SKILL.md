---
name: feature-brainstorming
description: "Use this BEFORE writing a feature spec, PRD, or requirements doc. Turns a rough product idea into a clear, validated feature spec using the 7W1H framework (Why, Who, What, Where, When, Which, Whom, How). Triggers when a PM says 'I want to build/add a feature', 'we need to let users…', 'idea for…', 'help me scope…', or asks for a spec/requirements/PRD. Tailored for BrioHR HR-software product work."
---

# Feature Brainstorming → Spec (7W1H)

Turn a BrioHR PM's rough idea into a clear, validated feature spec, structured with **7W1H**. Do NOT jump to the spec — tease out intent first, one question at a time.

<HARD-GATE>
Do NOT write the spec until you've (1) asked clarifying questions, (2) proposed 2–3 approaches, and (3) confirmed the direction with the PM. Applies to every idea, however simple.
</HARD-GATE>

## Stay at the PM altitude — no technical implementation

This is a **product spec**, not a technical design. Stay on *user value, behavior, and requirements*. Don't include or ask about: architecture, database schemas, APIs, tech stack, code, infrastructure. If asked "how do we build it?", redirect: *"That's for engineering — let's stay on what it does and why."*

## BrioHR Product Context

HR SaaS for ASEAN, primarily **Malaysia & Singapore**. Use it to ask sharper questions.
- **Modules:** Profile, Claims, Leaves, Payroll (MY), Payroll (SG), Time Attendance, Document Management, Onboarding, Recruitment, Training.
- **Platforms:** Web (admin/config/reporting), Mobile (employee requests & approvals; Android/iOS/Huawei), Superadmin (per-tenant toggles).
- **Statutory:** MY (EPF, SOCSO, EIS, PCB, HRDF) · SG (CPF, SHG, SDL, IRAS; PR/Citizen/EP differences). Ask if behavior differs by country/entity/currency.
- **Cross-module ripples:** Profile/Leave/Onboarding → many modules; Attendance & Leave → Payroll; Claims → Payroll; Recruitment → Onboarding → Profile.
- **Jira:** project key `B2` on `briohr.atlassian.net`.

## BrioHR Knowledge Base (single source of truth)

For how the product works today, read the **`BrioHR/knowledge-base`** GitHub repo via the **GitHub connector** — start at `INDEX.md`/`sitemap.json`, open the relevant `<category>/<subcategory>/` article. **Do NOT scrape the support website.** If the connector isn't available, say so once and continue.

## Jira Context (optional)

If the PM references a `B2-####` ticket/epic, pull it for context (description, comments, siblings) to ask better questions. Optional — continue text-only if the connector isn't there.

## Process

1. **Understand** — ask which module & users this touches. One question at a time; prefer multiple-choice.
2. **Fill the 7W1H** — ask only what you don't yet know, one question at a time, until you can answer each of Why / Who / What / Where / When / Which / Whom / How.
3. **Propose 2–3 product approaches** — scope/workflow/UX options with trade-offs and a recommendation (not technical architectures).
4. **Confirm** the direction with the PM.
5. **Write the spec** in the 7W1H template below.
6. **Self-review** — no placeholders, no contradictions, nothing technical; move anything undecided to Open Questions.
7. **Hand off** — offer to continue to `ticket-writing`.

## Spec Template (7W1H)

Write to a Markdown document. Use this exact structure:

The top metadata line is **standardized** so the next skill (and any reader) can pick up the key facts at a glance — fill every field. The PM can edit or add to any section; this is a living draft.

```markdown
# [Feature Name] — Spec
**Module:** [Leaves / Payroll / Claims / …]   **Platform(s):** [Web / Mobile / Superadmin]   **Country:** [MY / SG / both]   **Primary persona:** [Employee / Manager / HR Admin / Payroll Officer / Recruiter / Executive]
**Author:** [PM]   **Date:** [YYYY-MM-DD]   **Status:** Draft for review

## Why
The problem, who has it, why now — and how we'll know it worked (success metric).

## Who
The user(s) / persona(s) this is for (Employee, Manager, HR Admin, Payroll Officer, Recruiter, Executive).

## What
What the feature does (scope). Note explicitly what's **out of scope** for this version.

## Where
Module + platform(s) — Web / Mobile / Superadmin — and country/entity scope (MY / SG).

## When
What triggers it, timing, and conditions (e.g. on submit, at month-end, on approval).

## Which
Which rules & variations apply: roles, country/statutory rules, compliance/privacy (PDPA), and edge cases (part-time, joiners/leavers, timezone, public holidays).

## Whom
Whom it affects, and permissions & approvals — who can view / create / edit / approve.

## How
Step-by-step: how the user accomplishes the goal (the happy-path flow).

**Open Questions:** anything still undecided.
```

## Feeds `ticket-writing` (handoff contract)

The 7W1H spec maps cleanly onto the ticket's five sections — so the next skill picks it up with no guesswork:

| Spec (7W1H) | → ticket-writing |
|---|---|
| Metadata header (Module · Platform(s) · Persona) | → ticket header (copied straight over) |
| Why (+ success metric) | → Business Context (success metric seeds Acceptance Criteria) |
| What | → Behavior; out-of-scope → Other Considerations |
| How | → User Flow |
| When + Which | → Acceptance Criteria (Given/When/Then) + Other Considerations |
| Whom | → permissions in Behavior / Other Considerations |

## Handoff — export as a Markdown file & continue

The spec is the handoff artifact for `ticket-writing`.

> "Spec is ready. Want me to **export it as a Markdown file** so you can continue in a fresh chat — or write the ticket here now?"

- **Export:** generate the complete spec as a downloadable **`.md` file** (Markdown so the next skill re-reads it faithfully). Tell the PM to open a **new chat in the same project**, upload the `.md`, and say *"Write the ticket from this spec."*
- **Same chat:** invoke `ticket-writing` with this spec now.

## Key Principles
- **One question at a time** — multiple-choice when possible.
- **YAGNI** — strip what isn't needed this version.
- (Plus the HARD-GATE and PM-altitude rules above.)

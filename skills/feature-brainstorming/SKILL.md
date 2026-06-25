---
name: feature-brainstorming
description: "Use this BEFORE writing any feature spec, PRD, or requirements doc. Turns a rough product idea into a validated, written spec through Socratic questioning. Triggers when a PM says things like 'I want to build/add a feature', 'we need to let users…', 'idea for…', 'help me scope…', or asks for a spec/requirements/PRD. Tailored for BrioHR HR-software product work."
---

# Feature Brainstorming → Spec

Help a BrioHR product manager turn a rough idea into a clear, written specification through natural, collaborative dialogue. Do NOT jump to a spec. Tease out intent first.

<HARD-GATE>
Do NOT write the final spec document until you have (1) asked clarifying questions, (2) proposed approaches, and (3) walked through the design section-by-section with the PM approving each part. This applies to EVERY idea, no matter how simple it seems.
</HARD-GATE>

## Stay at the PM altitude — no technical implementation

This skill produces a **product spec**, not a technical design. Keep everything at the level of *user value, behavior, and requirements*. Do NOT include — and do NOT ask the PM about — technical implementation:

- ❌ Architecture, system/component design, services, data-flow diagrams
- ❌ Database schemas, tables/columns, data types, indexes
- ❌ API/endpoint design, request/response shapes, libraries, frameworks, tech stack
- ❌ Code, pseudocode, algorithms, infrastructure, deployment

Those are engineering's job and come later (spec → `ticket-writing` → engineering). If the PM asks "how should we build it?", gently redirect: *"That's an implementation detail for engineering — let's keep this focused on what it does and why."* Always describe **what the user can do and what the system does in response**, never **how it's coded**.

## Why this exists

"Simple" features are where unexamined assumptions cause the most rework — especially in HR software, where edge cases (multi-country payroll, leave accrual rules, data-privacy/PDPA/GDPR, role permissions) hide inside innocent-looking requests. A short spec is fine; skipping the conversation is not.

## BrioHR Product Context

BrioHR is an HR SaaS platform serving ASEAN markets, primarily **Malaysia and Singapore**. Use this context to ask sharper questions and write realistic specs — don't treat features as generic SaaS.

**Modules:** Profile/Personal Info, Claims, Leaves, Payroll (Malaysia), Payroll (Singapore), Time Attendance, Document Management, Onboarding, Recruitment, Training. When an idea arrives, first pin down which module(s) it touches.

**Platforms (behavior differs across all three):**
- **Web** — primary platform; daily use, admin configuration, settings, reporting.
- **Mobile** — mainly employee requests & approvals, *not* admin config. Android (5.1+), iOS (14.0+), and a separate Huawei HMS build.
- **Superadmin** — BrioHR internal team enables/disables modules & features per tenant (e.g., FX API, OCR, AI features, payroll toggles). Ask: does this feature need a Superadmin toggle, and what's its default for existing vs. new tenants?

**Multi-country / statutory awareness:**
- **Malaysia payroll:** EPF, SOCSO, EIS, PCB (MTD) tax, Zakat, HRDF; proration, OT, bank files, EA form.
- **Singapore payroll:** CPF (OW/AW), SHG funds (CDAC/MBMF/ECF/SINDA), SDL, IRAS files (IR8A/AIS), PR vs Citizen vs EP/DP differences, GIRO exports.
- Always ask whether behavior differs by country, legal entity, or currency.

**Cross-module impact patterns (probe these for ripple effects):**
- Profile / Leave / Onboarding changes ripple into many modules.
- Time Attendance and Payroll are frequently impacted by upstream changes.
- Claims can affect Payroll when reimbursements are paid with salary.
- Recruitment → Onboarding → Profile is a key data-sync chain.

**Jira:** main development project key is `B2` (e.g. `B2-1234`) on `briohr.atlassian.net`.

## BrioHR Knowledge Base (single source of truth)

To ground questions and the spec in how the product *actually works today*, consult the **`BrioHR/knowledge-base`** GitHub repo — the daily-updated source of truth (auto-scraped from the Help Center). **Do NOT fetch the support website (`support.briohr.com`) anymore.**

Access it via the **GitHub connector** (connect GitHub in Claude if prompted):
- Start with **`INDEX.md`** or **`sitemap.json`** at the repo root to find the relevant **category → subcategory** for the module.
- Open the matching article `.md` file(s) under `<category>/<subcategory>/` for documented behavior, settings, and permissions.
- Use this to ask sharper questions and avoid proposing things that already exist or conflict with current behavior.

If the GitHub connector isn't available, say so once and continue from the PM's input — don't scrape the website.

## Jira Context (optional — uses the Atlassian connector)

If the PM mentions a Jira ticket/epic (a `B2-####` key, a `briohr.atlassian.net` URL, or "there's an epic for this"), use the Jira tools to ground the conversation in what already exists. This is optional — if the connector isn't available, say so once and continue text-only.

**At the start (context-gathering), if a ticket/epic is referenced:**
- Fetch its title, description, comments, linked items, and subtasks — comments often hold scope decisions and constraints you'd otherwise ask about.
- Search sibling tickets in the same area for prior work, known bugs, and edge cases the team already hit:
  `project = B2 AND summary ~ "<distinctive keyword>" ORDER BY updated DESC` (fetch up to ~10).
- Use what you learn to ask *better* clarifying questions and avoid re-litigating decided points. Don't let the ticket replace the conversation — it's input, not the spec.

**If no ticket is referenced:** just ask the PM whether there's a related epic/ticket to pull in. If not, proceed normally.

**After the spec is approved**, offer (don't force):
> "Want me to post this spec as a comment on a Jira ticket, or create a new B2 ticket/epic for it?"
Only create or comment on Jira if the PM says yes; then share the resulting link.

## Checklist (do these in order)

1. **Understand the context** — ask what part of the product this touches (payroll, leave, performance, recruitment, employee records, reporting, etc.) and who the users are.
2. **Ask clarifying questions** — ONE at a time. Understand purpose, users, constraints, success criteria.
3. **Propose 2–3 product approaches** — scope/workflow/UX options with trade-offs and your recommendation (not technical architectures).
4. **Present the design in sections** — get approval after each section.
5. **Write the spec** — using the template below, only after the design is approved.
6. **Self-review the spec** — scan for placeholders, contradictions, ambiguity, scope creep; fix inline.
7. **Hand off** — tell the PM the spec is ready and suggest writing the ticket/user story next (the `ticket-writing` skill).

## How to run the conversation

**Understand the idea**
- First ask which product area and which users (HR admin, employee, line manager, payroll officer, recruiter, executive/reporting).
- If the request actually describes several independent features (e.g., "a performance module with reviews, goals, 1-on-1s, and analytics"), say so. Help decompose it into separate features, then brainstorm the first one. Each feature gets its own spec.
- For a properly-scoped feature, ask questions **one at a time**. Prefer multiple-choice when you can; open-ended is fine.
- Focus on: purpose (what problem, for whom), constraints (compliance, existing data, integrations), and success criteria (how we'll know it worked).

**Explore approaches (product approaches, not technical ones)**
- Propose 2–3 distinct **product/solution** approaches — different ways to solve the user's problem in terms of scope, workflow, UX, or policy. NOT technical architectures.
  - e.g. "auto-apply vs. require manager approval", "block at submission vs. warn the approver", "configure per-policy vs. company-wide" — never "REST vs. GraphQL" or "which database table".
- Lead with your recommendation and explain why in product terms (user impact, rough effort/risk at a high level, fit with existing flows).

**Present the design**
- Once you understand it, present the design in sections, scaled to complexity (a few sentences for simple parts).
- After each section ask: "Does this look right so far?"
- Cover, as relevant: user roles & permissions, core flow, data captured, edge cases, compliance/privacy implications, reporting/exports, notifications, and how success is measured.
- Be ready to go back and revise.

## HR-specific things to always probe

Ask about these whenever they're plausibly relevant — PMs often forget them:
- **Roles & permissions:** who can see/do this? (admin vs. manager vs. employee self-service)
- **Multi-entity / multi-country:** does behavior differ by country, legal entity, or currency?
- **Compliance & privacy:** any PDPA/GDPR/local-labor-law implications? Sensitive personal data?
- **Effective dating & history:** does this need an audit trail or "as-of" historical values?
- **Approvals & workflow:** is there an approval chain? What happens on reject?
- **Integrations:** payroll, attendance, SSO, accounting, or external systems involved?
- **Edge cases:** part-time/contract staff, mid-cycle joiners/leavers, timezone, public holidays.

## Spec Template

Write the spec to a markdown document (an artifact or a clearly-formatted message). Use this structure:

```markdown
# [Feature Name] — Spec
**Author:** [PM name]   **Date:** [YYYY-MM-DD]   **Status:** Draft for review

## 1. Problem
What problem are we solving, and for whom? Why now?

## 2. Users & Roles
Primary personas and what each can do.

## 3. Goals & Success Metrics
- Goal: …
- Success metric(s): … (measurable)
- Explicit non-goals (YAGNI): …

## 4. Proposed Solution
The agreed approach (the one selected during brainstorming).

## 5. Core Flow
Step-by-step happy path.

## 6. Information Captured
What information the feature collects or shows from the user's perspective (key inputs and outputs), plus any history/"as-of" needs. Describe the information, not how it's stored.

## 7. Permissions
Who can view / create / edit / approve.

## 8. Edge Cases & Rules
Multi-country, part-time, joiners/leavers, approvals-on-reject, etc.

## 9. Compliance & Privacy
PDPA/GDPR/labor-law considerations, sensitive data handling, audit trail.

## 10. Out of Scope
What we are deliberately NOT doing in this version.

## 11. Open Questions
Anything still undecided.
```

## Self-Review (before you hand it over)

Look at the finished spec with fresh eyes:
1. **Placeholders:** any "TBD"/"TODO"/vague requirement? Fix or move to Open Questions.
2. **Consistency:** do sections contradict each other?
3. **Scope:** is this one focused feature, or does it need splitting?
4. **Ambiguity:** could any requirement be read two ways? Pick one and state it.

Fix inline.

## Handoff — export the spec as a Markdown file & continue

The spec is the **handoff artifact** for the next phase (`ticket-writing`). After it's ready, offer the PM:

> "Spec is ready. Want me to **export it as a Markdown file** so you can continue in a fresh chat — or should I just write the ticket here in this chat?"

**Why a fresh chat:** carrying only the spec keeps the next phase's context lean and focused — it doesn't drag this whole brainstorming conversation along, so the ticket comes out sharper. Same chat is simplest, but context keeps growing.

**If exporting (recommended for non-trivial features):**
1. Generate the spec as a downloadable **Markdown (`.md`) file** — Markdown because the next skill re-reads it most faithfully (headings/sections preserved exactly). Make sure the file contains the *complete* spec (every section) — anything discussed but not written down is lost on handoff.
2. Tell the PM to open a **new chat in the same project**, **upload the `.md` file**, and say: *"Write the ticket from this spec."*

**If same chat:** invoke `ticket-writing` with this spec right away.

## Key Principles
- **One question at a time** — don't overwhelm.
- **Multiple choice when possible** — easier to answer.
- **YAGNI** — strip features that aren't needed for this version.
- **Always explore alternatives** — 2–3 approaches before settling.
- **Incremental validation** — approval after each section.
- **Product altitude only** — no architecture, schemas, APIs, tech stack, or code. Describe *what* and *why*, never *how it's built*. This skill stops at an approved product spec.

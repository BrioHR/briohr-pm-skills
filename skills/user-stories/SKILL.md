---
name: user-stories
description: "Use to turn a feature, spec, or requirement into well-formed user stories with Given/When/Then acceptance criteria. Triggers when a PM says 'write user stories', 'acceptance criteria', 'break this into stories', 'Gherkin', 'tickets for eng', or pastes a spec/feature description and wants it decomposed for engineering. Tailored for BrioHR HR-software personas."
---

# User Stories & Acceptance Criteria

Turn a feature or spec into a set of clear, independent user stories that an engineer with no product context could pick up and build. Each story gets testable acceptance criteria in Given/When/Then form.

## Before you write anything

1. **Get the source.** Ask the PM for the feature/spec (or the brainstorming spec doc). If it's vague, ask 1–3 clarifying questions first — do NOT invent requirements.
2. **Confirm the personas.** Default BrioHR personas: **Employee**, **Line Manager**, **HR Admin**, **Payroll Officer**, **Recruiter**, **Executive/Reporting viewer**. Confirm which apply.
3. **Confirm scope.** What's in this version vs. later (YAGNI). Don't write stories for out-of-scope behavior.

## Story format

Each story uses this exact shape:

```markdown
### [Short title]
**As a** [persona]
**I want** [capability]
**So that** [benefit/outcome]

**Acceptance Criteria**
- **Given** [context] **When** [action] **Then** [observable result]
- **Given** … **When** … **Then** …

**Notes**
- Permissions: who can do this
- Edge cases / out of scope
- Dependencies (other stories, integrations)
```

## Rules for good stories

- **One capability per story.** If "and" sneaks into the *I want* line, split it.
- **INVEST:** each story should be Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Vertical slices, not layers.** A story delivers user-visible value end-to-end — never "build the database table" as its own story.
- **Acceptance criteria are testable.** Every Then must be observable. No "works correctly" or "is fast" — state the actual expected behavior or threshold.
- **Cover the unhappy paths.** For each story add criteria for: validation errors, empty/zero state, permission denied, and the most likely failure.

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
2. **The full stories** — using the format above, grouped by persona or by flow.
3. **Gap check** — a short "Did we miss anything?" section calling out personas, edge cases, or compliance items that have no story yet, so the PM can decide whether to add them.

## Self-review before handing over

- Does every acceptance criterion have an observable Then?
- Is every persona from scope covered by at least one story?
- Did you include unhappy-path criteria (validation, permissions, empty state)?
- Are any stories actually two stories? Split them.
- Are out-of-scope items explicitly listed, not silently dropped?

Then offer:
> "Here are the stories. Want me to format these as a table for import (Jira/Linear), tighten any story, or add edge-case coverage?"

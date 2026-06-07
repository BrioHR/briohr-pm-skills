# Test Case Preparation Checklist

This is the canonical six-section checklist for BrioHR test case generation. Use it during Step 4 (sequential confirmation) and Step 5 (test case drafting) of the workflow.

For each section, the bullet points are the **prompts to consider** when drafting scenarios — they are not test cases themselves. Translate each relevant prompt into one or more concrete, BrioHR-specific scenarios grounded in the ticket context.

---

## 1. Initialization & Migration

**One-line summary for the PM:** "Covers data migration, default values, and impact on existing records."

**Prompts to consider when drafting:**
- Is data migration needed for existing tenants/customers?
- Any default value or backfill required for new fields, settings, or columns?
- Any existing data impacted (records that need to be re-evaluated, recomputed, or re-displayed)?
- Are there migration rollback considerations?
- Does the change affect data created before the release vs. after?
- If the ticket touches a Superadmin toggle: what is the default state (ON/OFF) for existing tenants vs. new tenants?

---

## 2. Regression

**One-line summary for the PM:** "Covers existing flows that could break and old behavior that must still work."

**Prompts to consider when drafting:**
- What existing flows in the same module could be affected?
- Which old behavior must still work exactly as before?
- Any permission or role impact (Admin, HR, Manager, Employee)?
- Any cross-feature regression risk? Use the known cross-module patterns:
  - Profile/Leave/Onboarding changes can ripple into many other modules
  - Time Attendance and Payroll are frequently impacted by upstream changes
  - Claims can affect Payroll when reimbursements are paid with salary
- Does the change touch shared components used across modules?
- Does behavior differ between Web, Mobile, and Superadmin — and do all three remain consistent after the change?

---

## 3. Happy Flow / Smoke Test

**One-line summary for the PM:** "Covers the main user flow end-to-end with the primary success path."

**Prompts to consider when drafting:**
- Main user flow works end-to-end (the core scenario the ticket is about).
- Create / update / delete / view behavior for the primary entity.
- Success messages, redirects, and status changes after each action.
- Default user role (typically the role the feature is designed for) completes the flow without errors.
- Required vs. optional fields behave correctly on submit.
- For payroll-related flows: use the standard BrioHR salary test ranges (MYR 1,500 / 5,000 / 15,000 / 40,000 for Malaysia; SGD 2,000 / 6,000 / 12,000 / 30,000 for Singapore).

---

## 4. Integration / Interaction

**One-line summary for the PM:** "Covers interaction with other modules, APIs, notifications, emails, reports, and exports."

**Prompts to consider when drafting:**
- Any interaction with other BrioHR modules? Prioritize these known high-impact pairs:
  - Leave changes affecting Payroll deductions
  - Time Attendance changes affecting Payroll computation
  - Claims changes affecting Payroll reimbursement payouts
  - Onboarding/Recruitment changes affecting Profile data
  - Profile changes affecting Leave entitlements or Payroll employee records
- Any API or webhook impact (request/response shape, new fields, breaking changes)?
- Any notification, email, or in-app alert triggered or changed?
- Any report, dashboard widget, or export (CSV/Excel/PDF) affected?
- Any third-party integration (calendar, SSO, accounting, payroll provider) involved?
- If the feature is enabled via Superadmin: does it interact differently with other modules when toggled on vs. off?

---

## 5. Platform Coverage

**One-line summary for the PM:** "Covers whether and how the change behaves across Web, Mobile, and Superadmin."

**Prompts to consider when drafting:**

**Web app (primary platform):**
- Does the full feature work correctly on the web, including all admin configuration and settings?
- Are all UI states (loading, empty, error, success) handled?

**Mobile app:**
- Does the feature require a mobile app update, or is it web-only?
- Does mobile need testing even if no mobile code change was made (e.g., the API or data model changed)?
- Android-specific behavior to verify (Android 5.1+ minimum).
- iOS-specific behavior to verify (iOS 14.0+ minimum).
- Huawei HMS build behavior to verify (separate build from Android Play Store).
- Push notifications on mobile if relevant.
- Remember: mobile is primarily for employee submissions and approvals, not admin configuration. Do not include admin-only steps in mobile test cases.

**Superadmin:**
- Does this feature have a Superadmin toggle or setting?
- Verify behavior when the feature is enabled vs. disabled at the tenant level.
- Verify that enabling/disabling via Superadmin takes effect immediately (or on next session, whichever is documented).

---

## 6. Edge Cases

**One-line summary for the PM:** "Covers empty states, invalid input, permission denied, large data, failed APIs, and timezone/date handling."

**Prompts to consider when drafting:**
- Empty state (no data, first-time user, no records to display).
- Invalid input (wrong format, out-of-range values, special characters, very long strings).
- For numeric/salary fields: include negative, zero, and boundary values.
- Permission denied (a role that should not see or access this feature — e.g., Employee trying to access an HR-only screen).
- Large data sets and pagination behavior.
- Failed API call, network timeout, and loading state visibility.
- Timezone and date handling (DST transitions, cross-timezone users, end-of-month, leap year, public holidays).
- Concurrent edits or stale data scenarios where relevant.
- Malaysia and Singapore statutory edge cases where applicable (e.g., EPF rate changes, CPF wage ceiling, mid-month joiners, resignation mid-cycle).

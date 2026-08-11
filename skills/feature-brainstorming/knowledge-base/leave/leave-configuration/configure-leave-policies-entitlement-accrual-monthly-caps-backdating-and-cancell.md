---
title: "Configure Leave Policies: Entitlement Accrual, Monthly Caps, Backdating and Cancellations"
category: "Leave"
subcategory: "Leave Configuration"
source_url: "https://support.briohr.com/knowledge/configure-leave-policies-entitlement-accrual-monthly-caps-backdating-and-cancellations"
date: "August 11, 2026"
---

# Configure Leave Policies: Entitlement Accrual, Monthly Caps, Backdating and Cancellations

*How leave entitlement accrues monthly, why an employee's balance can look lower than the policy, monthly application caps, backdating limits, and how cancellations work.*

**How entitlement accrual and proration work**


When a leave policy uses Earned Leave, employees earn their entitlement progressively through the year instead of receiving it upfront:


**Entitlement ÷ 12 months × months worked in the calendar year = current accrued leave balance**


Example: an employee with a customised 7-day entitlement, checked in July → 7 ÷ 12 × 7 = 4.08 days accrued.


Two things to know:


- Proration always uses the employee's **Join Date**.
- If an employee's balance looks lower than the policy's entitlement number (e.g. "policy says 6 days but the employee sees 3"), check whether **Earned Leave** is enabled — the employee may simply not have accrued the full amount yet. To grant the full entitlement upfront instead: Disable **Earned Leave (Monthly Basis)**.


**Cap what employees can apply per month**


To prevent staff from applying more leave than they have earned so far:


1. Go to **HR Lounge > Leave > Leave Type & Policies**, click **View Details** for the selected Leave Type.
2. Select the relevant policy, go to **General Configuration > Entitlement**.
3. Under **Earned Leave**, select **Monthly Basis** (accrues Annual Entitlement ÷ 12 each month).
4. Make sure **Enable Tolerance Amount** is disabled (or the limit is set to 0), so employees cannot apply beyond their earned balance.
5. **Save Settings.**


**Backdated leave — what the application window can and cannot do**


- **Allow employee to apply leave in the past** (Leave Advanced Settings) is an optional function. When ON, employees can submit backdated applications at any time within the current calendar year.
- There is no setting to limit backdating to a specific number of days (e.g. "must apply within 2 days after the leave started"). Workaround: enforce the rule through your company policy — backdated applications still go through approval, so the manager or HR can check the submission date and reject or query anything outside your window.


**Leave cancellation — who approves, when the balance comes back**


- When an employee cancels a future-dated leave: the status changes to **Cancelled** immediately, the balance is credited back automatically at the same time, and the cancelled leave does not require Manager approval.
- For past dates, HR/Admin cancels on the employee's behalf; the balance is restored once the cancellation is processed.
- To control whether employees can cancel their own leaves: this is a User Group permission, only accessible by the HR admin — **Settings > User Group > Edit** on the Employee user group **> Employee Modules Permission > Leave >** enable/disable the permission to **Cancel their own leaves**.


**FAQ**


**Q: Can we delete a leave type or a leave policy we no longer use? Do we lose history?**


Leave *types* cannot be deleted by clients — only leave *policies* can. (If a leave type itself must be removed, contact support so the product team can handle it.) Deleting a leave policy does **not** erase historical records: the policy is no longer visible to employees, but all previous leave applications remain visible in the system and dashboards.


If you prefer not to delete the policy, you can disable it instead:


1. Go to **HR Lounge > Leave > Leave Type & Policies**, click **View Leave Details** for the leave type.
2. Click **Assign Policy** under Tools, select the employees (or tick select-all).
3. Set the policy dropdown to **"Not Applicable"** and click **Apply**.


This hides the leave type from dashboards (no new applications) while keeping all past records and entitlements for employees.


**Q: How do I add Unpaid Leave as a Leave option?**


Create it as a new Leave Type:


1. Go to **HR Lounge > Leave > Leave Types & Policies**
2. Click **+ Create Leave Type** and configure its policy
3. In **Tools**, assign the policy to the relevant employees


**Q: How do I assign a leave policy to a new joiner?**


1. Go to **HR Lounge > Leave > Leave Types & Policies**
2. Select the Leave Type
3. In **Tools**, click **Assign Policy**
4. Select the employee's name and assign the relevant policy


Supporting article: [Streamline Your HR Process: Assigning Leave Policies to Employees](https://support.briohr.com/knowledge/streamline-your-hr-process-assigning-leave-policies-to-employees?hsLang=en)


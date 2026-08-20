---
title: "Offboarding Payroll and Leave: Final Pay, Tax Clearance Holds, Encashment and Cycle Order"
category: "Payroll"
subcategory: "Payroll Management"
source_url: "https://support.briohr.com/knowledge/offboarding-payroll-and-leave-final-pay-tax-clearance-holds-encashment-and-cycle-order"
date: "August 20, 2026"
---

# Offboarding Payroll and Leave: Final Pay, Tax Clearance Holds, Encashment and Cycle Order

*What happens when you set an Employment End Date, how final pay and leave are prorated, handling tax-clearance salary holds (CP21/IRAS), AL encashment, and the payroll cycle order.*

**What happens when you set the Employment End Date**


- If the date is in the future, nothing changes immediately — the account stays active until the date passes.
- Once the end date passes: the account automatically becomes Inactive (no more login), and the system prorates the leave balance and salary based on the end date. The profile remains in the system for historical and reporting purposes.
- To enter it: **Employee Profile > '...' (ellipsis) > End Employment >** enter the date and save. The leave entitlement recalculates automatically per the leave policy's proration rules.


**The payroll cycle order rule**


Only one payroll cycle can be ongoing at a time. So if you run a separate cycle for resigned staff, complete that cycle first — only then can the regular monthly cycle run. You can also run your regular monthly cycle first, complete it, then run the cycle for resigned staff. The order does not matter in this scenario, only that you complete the previous cycle before starting a new one. See [How to Process Salaries for Terminated Employees in a Separate Payroll Cycle](https://support.briohr.com/knowledge/how-to-process-salaries-for-terminated-employees-in-a-separate-payroll-cycle?hsLang=en).


**Salary withheld pending tax clearance (CP21 / IRAS21 for departing foreign employees)**


Typical flow when you hold the final salary until the clearance letter arrives:


1. Exclude the employee from the current payroll cycle.
2. After the end date passes, the employee becomes Inactive and will not appear in later cycles by default.
3. When the clearance letter arrives, add the employee to a cycle (or create an Ad-hoc cycle), enter the withheld amount manually (e.g. as Arrears of Salary), then complete the payroll and release the payslip.


**Annual-leave encashment for a resignee**


Set the Employment End Date first — the system prorates the entitlement — then read the remaining balance from the profile. The encashment amount itself is a manual calculation added to the final payroll. See also [How To Process Leave Encashment When An Employee Resigns](https://support.briohr.com/knowledge/how-to-process-leave-encashment-when-an-employee-resigns?hsLang=en).


**FAQ**


**Q: Can I simulate a future month's payroll to tell a resignee their final amount?**


Yes — you can run the future cycle to see the calculation and then delete it (HR/Admins can delete cycles self-serve once the permission is enabled — see [Delete Latest Payroll Cycle in Current Payroll Month](https://support.briohr.com/knowledge/delete-latest-payroll-cycle-in-current-payroll-month?hsLang=en)). Two cautions: complete the intermediate months in sequence first, and do NOT submit any payout, bank or statutory files from a simulation run — some portals reject a second upload of the same file.


**Q: Resigned staff still appear in my bulk-import employee list — can we archive them?**


No — resigned employees cannot be permanently deleted or archived (records are kept for audit). Just delete their rows in the Excel file before uploading; this does not affect their profiles.


**Q: In the resigned-staff cycle, the basic salary shows 0 and is not prorated. What should I check?**


Go to the employee's profile > Payroll > Payroll cycle section. Ensure that the employee is actually in the terminated/resigned cycle (box is ticked), and salary allocation is set correctly (set to 100% for the terminated/resigned cycle). If the proration is incorrect, double-check that the end employment date set is correct.


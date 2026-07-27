---
title: "Update Rosters and Timesheets After a Work Schedule Change"
category: "Time Attendance"
subcategory: "Time Attendance Management"
source_url: "https://support.briohr.com/knowledge/update-rosters-and-timesheets-after-a-work-schedule-change"
date: "July 27, 2026"
---

# Update Rosters and Timesheets After a Work Schedule Change

*Changing a work schedule or shift may not update rosters and timesheets that already exist — this article explains how to reset the roster and recalculate the timesheet.*

** Audience & Scope**

- Audience: **HR Admin**
- Module: **Time & Attendance (Rostering, Timesheet, Daily Attendance)**
- Prerequisites: **HR Lounge access to Time & Attendance**
- When to use this article: You assigned a new work schedule, but the roster still shows the old one; you corrected a schedule's hours, but the timesheet still calculates with the old hours (e.g. a negative difference); multiple shifts appear on the roster; you need to update the rostering for staff.


[](#key-behaviour-why-this-happens)**Key behaviour (why this happens)**

Changes to a Work Schedule or Shift may not automatically update rosters or timesheets that were already generated with the previous settings. The existing roster may stay unchanged until it is reset; the timesheet recalculates only after the roster is updated.


[](#reset-the-roster-after-a-schedule-change)**Reset the roster after a schedule change**

1. Go to HR Lounge > Time & Attendance > Rostering.
2. Select the affected employee and the relevant period/dates.
3. Reset (or remove/replace) the existing roster assignment. — the system regenerates the roster from the newly assigned work schedule.
4. Assign the updated shift/schedule where needed.
5. Click Publish Rostering (if not yet published).


Note: the roster update can be done in bulk (choose multiple employees, or Reset All). Be careful with the ‘Reset All’ button; it will reset all schedules that were manually added/edited.


[](#if-an-attendancetimesheet-entry-is-already-linked-to-the-shift)**If an attendance/timesheet entry is already linked to the shift**

The system prevents removing a roster shift that has a linked attendance entry. In that case:


1. Take a screenshot of the employee's current First In / Last Out times for the affected date (so you can restore them).
2. In Time & Attendance > Daily Attendance (or Timesheet), open the entry with the pencil (Edit) icon and select Clear entries to remove the clock-in/out, then save.
3. Return to Rostering, replace the incorrect shift with the correct one, and click Publish Rostering (if not yet published).
4. Go back to Daily Attendance / Timesheet and re-enter the original clock-in/out times from your screenshot, then save.


The timesheet then recalculates on the updated schedule.


[](#common-issues--faq)**Common Issues / FAQ**

- **Q:** **The timesheet was already approved or processed in payroll — can I still fix it?**
**A:** Reopen the timesheet first if the timesheet is in ‘Approved’ status (Re-open for just that employee/period — weekly or monthly view), then make the roster changes. If the timesheet has been sent to payroll, you will need to exclude the timesheet from a payroll run first (done in the Payroll module) before you can reopen the timesheet.
- **Q:** **Why do I see two shifts on the same day?**
**A:** BrioHR allows up to 2 non-overlapping shifts per day. A second shift usually appears because a new shift was added instead of replacing the old one, a half-day leave split the shift (Half-Day Leave Handling settings), or a pre-approved OT used "Add time slot instead". Replace/remove the unwanted shift in Rostering and republish.
- **Q:** **The roster keeps re-generating with wrong shifts for everyone — is that the same issue?**
**A:** If replacing and republishing doesn't stop it, contact support — this may need account-level investigation.


[](#related-articles)Related Articles

- [How HR/Admin Manage Rostering of All Employees](/knowledge/how-hr/admin-manage-rostering-of-all-employees?hsLang=en)


---
title: "How to Create and Configure Leave Policies in BrioHR"
category: "Leave"
subcategory: "Leave Configuration"
source_url: "https://support.briohr.com/knowledge/how-to-set-up-leave-policies"
date: "May 4, 2026"
---

# How to Create and Configure Leave Policies in BrioHR

*Learn how to create, configure, and customize leave policies in BrioHR. This detailed guide covers policy availability, approval flow, entitlements, carry forward rules, and advanced settings.*

### Introduction


Creating tailored leave policies ensures that your company’s leave management reflects the needs of various teams, offices, and employment levels. BrioHR allows you to set up multiple **leave policies** under one **leave type**, each with distinct rules and configurations.


For example, you might apply different annual leave rules for employees in your **Thailand office** versus those in **Indonesia**, or vary entitlements based on **job grades**.
Each **leave policy** is fully customizable and can differ significantly from others.[](https://support.briohr.com/knowledge/how-to-create-and-manage-your-employee-leave-types?hsLang=en)


Learn More: [How to Create and Manage Leave Types in BrioHR](https://support.briohr.com/knowledge/how-to-create-and-manage-your-employee-leave-types?hsLang=en)


---


### Step-by-Step Guide: Create a Leave Policy


#### Step 1 - Log In to BrioHR Account


Log in to your BrioHR account using your registered credentials.


#### Step 2 - Access the Leave Module and Policies


1. Go to **HR Lounge **> **Leave.**


2. Navigate to** Leave Types & Policies**.


3. Click **View Details** for the leave type where you want to add a new policy.


4. Under **Policy Configuration**, choose one of the following options:


- **Duplicate Existing Policy: **Quick setup when the new policy shares similar rules.
- **Add New Policy** : Start from scratch.


[Embedded content](https://www.loom.com/embed/42b3b4b59f7a47b5828f7eac74d53274)


---


### Step-by-Step Guide: Configure a Leave Policy (General Configuration)


The leave policy configuration consists of two parts:


1. **General Configuration**: Applies to all employees assigned to this policy.
2. **Custom Configuration**: For exceptions or employee-specific rules.


#### Step 1 - Configure Policy Availability


This section defines **who can be assigned** to a specific policy.

Note that setting availability does not automatically assign employees — you’ll still need to manually assign the policy.


Learn More: [How to Assign Leave Policies to Employees in BrioHR](/knowledge/streamline-your-hr-process-assigning-leave-policies-to-employees?hsLang=en)


You can make the policy:


- **Available to all employees**: Assign this policy to anybody in the company.
- **Only available to certain groups of employees**: Restrict this policy to a certain group of employees only such as:

  - Offices
  - Departments
  - Gender
  - Job Grades
  - Employment types


This restriction simplifies policy assignment when new employees join.


[Embedded content](https://www.loom.com/embed/51b066f9ce714491b728e0606137ec2b)


---


#### Step 2 - Configure the Leave Approval Process


When employees apply for leave, you can set an approval flow of up to **two steps.**


Each approver receives:


- An** email notification** and
- A **pending approval task **in the Pending Actions of BrioHR account


Approval options:


- **None: **Skip the step (e.g., for single-approver processes)
- **Position/Manager: **The employee's current manager approves the leave.
- **Specific Employee: **Assign a fixed approver manually.


**IMPORTANT NOTE:**

Approval steps are **sequential **- the second approver only receives the request after the first approval.


[Embedded content](https://www.loom.com/embed/e8f6999db71e46c288f5b533b8925ebc)


---


#### Step 3 - Configure the Entitlement Section


##### 3.1. Leave Entitlement


Choose first if you would like to have a leave entitlement. You have the following choices:


1. **Fixed Entitlement**: Assign a yearly leave quota (e.g., annual leave)

  1. Input the** Entitlement Amount** employees are entitled to per year.
2. **Upon Request**: No fixed quota; approval depends on management (e.g., Unpaid Leave)


**WARNING:**

If you put **"0"** as the **Entitlement Amount** (for Fixed Entitlement), the leave type will be** hidden** on employees' leave dashboard.

The employees won't be able to see the leave type option since they cannot apply for it.


##### Tolerance (Advance Days)


Enable tolerance if you allow employees to apply leave even with zero balance (**negative balance allowed up to the defined limit**)


For example,  if you choose a tolerance of 1, then the employee can still book 1 day if they have a leave balance of 0. This way, they will have a -1 leave balance until they earn new leaves. The way leave is earned is described in the next section.


**Learn More: **[How to Enable and Use the Tolerance Amount in BrioHR Leave Module](https://support.briohr.com/knowledge/enable-tolerance-amount-leave-module?hsLang=en)


![3-4-1](https://support.briohr.com/hs-fs/hubfs/3-4-1.png?width=670&height=205&name=3-4-1.png)


**Tip**:


Enable the Tolerance Amount feature in the Leave Policy settings to allow employees to apply for leave up to a set limit even when the balance is insufficient.


##### 3.2. Earned Leave


** **Earned leave allows you to set up leave to follow the accrual process throughout the year.


There are two types of earned leave:


- **Daily Basis: **The leave days are accrued or earned daily.

  - Calculation: Entitlement / 365 days
- **Monthly Basis:** The leave days are accrued or earned monthly.

  - Calculation: Entitlement/ 12 months


##### 3.2. Prorated Leave


Enable if entitlement should be adjusted for employees:


- Joining mid-year
- Leaving mid-year


Setting configuration:


- **Enabled**: The employees' entitlement is calculated based on the number of days/months they have worked in the company within the year. For example, applies to annual leave.
- **Disabled:** Full entitlement is given to the employees regardless they work full one year or not. For example, applies to replacement leave.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343964639/original/IQIJUpQ4hQV2QiCAVwGAlxs17lq4pCzWsg.png?1721286338)


Modes available:


- **Yearly Basis**: Prorate by Started, Completed, or Partial months.


**Learn More:** [Leave Proration Formula (Yearly Basis)](https://support.briohr.com/knowledge/leave-proration-formula-yearly-basis?hsLang=en)

- **Monthly Basis**: Prorate by percentage per month.


**Learn More:** [Prorate Leave on a Monthly Basis](https://support.briohr.com/knowledge/prorate-leave-on-a-monthly-basis?hs_preview=iTrGqiAC-175192438530&hsLang=en).

##### 3.3. Carry Forward Settings


##### Set rules for carrying unused leave into the next year:


- Define a maximum carry-forward limit
- Set an expiry date (e.g, 3 months after the year start, expiry date is 31 March)


##### BrioHR auto-calculates carry-forward at midnight on December 31, adding them into the initial balances for the new year.


**Learn More:**


- [How to Adjust Leave Balance or Carry Forward in BrioHR Leave Module](https://support.briohr.com/knowledge/how-to-adjust-leave-balance-or-carry-forward-in-hr-lounge?hsLang=en)
- [How to Enable Carry Forward Leave in BrioHR Leave Policies](/knowledge/how-to-enable-carry-forward-leave-in-briohr-leave-policies?hsLang=en)


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343965560/original/j0Wu8fGMHrwERt8gSkeqx_2L2D1XY1g4Yg.png?1721286797)


##### 3.4. Seniority (Years of Service)


Increase entitlement based on service duration.


Configure:


1. **Effective Date**:

  1. **Beginning of Period:** The incremental entitlement days will apply starting from **January, 1st** of the year following the employee's anniversary date.

    1. For example, if the employee joined in Dec 2016, and their entitlement is incremented by 1 day after 2 years of seniority, the employee will have the additional day available in 2019.
  2. **Anniversary: **The incremental entitlement days will apply on the anniversary day of the employee.

    1. On the anniversary date, the employee will be switching entitlement days during the year.
    2. Therefore, their yearly entitlement will be prorated between before and after the increment.
2. **Increment Mode: **

  1. **Fixed increment: **Define an increment and a frequency that will be applied.

    1. For example, +2 days every year, capped at 10 days.
  2. **Variable increment: **Set how many days to add after a certain number of years.

    1. For example, +2 days after 3 years, +1 day after 4 years


![3-7](https://support.briohr.com/hs-fs/hubfs/3-7.png?width=640&height=294&name=3-7.png)


**Learn More: **[Understanding Seniority Leave and Anniversary Dates](/knowledge/understanding-seniority-leave-and-anniversary-dates?hsLang=en)


Here is an example illustrating of the two modes of calculation methods:


![3-8](https://support.briohr.com/hs-fs/hubfs/3-8.png?width=670&height=682&name=3-8.png)


##### 3.5. Rounding Rules


Enable rounding to simplify entitlement calculations.


Learn More: [How to Calculate Entitlement with the Rounding Option Enabled.](https://support.briohr.com/knowledge/how-to-calculate-entitlement-with-the-rounding-option-enabled?hsLang=en)


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343966075/original/hQS4a9cKgWTs0n-vKCneTX12kbbSXjQ_nA.png?1721287044)


##### 3.6. Link to Another Leave Type


Share entitlement across multiple leave types.


Example: Link **Emergency Leave** to **Annual Leave **so both draw from the same balance.


**Learn More:** [How to Link Emergency Leave with Annual Leave Balance in BrioHR](https://support.briohr.com/knowledge/how-to-link-emergency-leave-with-annual-leave-balance-in-briohr?hsLang=en)


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343967598/original/-eJHfrf22gePXBdeo9iYv6Jk10bt98DU_A.png?1721287823)





---


#### Step 4 - Configure the Leave Advanced Settings


##### 4.1. Use working days


Determines how leave days are counted:


- **Enabled: **counts only working days based on employee's office schedule.


  - So if an employee does not work on weekends based on their office's configuration, if they book a leave from Friday to Monday, they will be deducted 2 days.
- **Disabled: **counts calendar days.

  - So if they book a leave from Friday to Monday, they will be deducted 4 days. This option is used for exceptional situations such as hospitalization leaves, or maternity leave.


![3-9](https://support.briohr.com/hs-fs/hubfs/3-9.png?width=670&height=50&name=3-9.png)


##### 4.2. Allow Booking Half Day


This setting determines whether the system allows employees to book half-day leaves:


- **Enabled: **employees can apply half-day leave.
- **Disabled:** only full-day leave allowed.


Learn More: [How to Manage Half-Day Leave for Employees](https://support.briohr.com/knowledge/how-to-manage-half-day-leave-for-employees?hsLang=en)


##### 4.3. Allow Employees to Apply for Past Leave


If enabled, employees will be able to apply for leaves on past days. This option can be used for medical leaves, for instance, when employees are not necessarily anticipating taking the leave.


##### 4.4. Allow Employees to Modify Past Leaves


This setting determines whether employees can modify the details of past approved leaves within the current year.


- **Enabled:** Allow employees to edit dates, justification, and attachment.


**IMPORTANT:**


- The modification will **require an approval process.**
- Employees **cannot modify the leave type**. If required to change the leave type, cancel the current leave and reapply a new leave using the desired leave type.





[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343969645/original/JgKNTIKX2NTcGgf39eVjwlSTDrNqRZ6E0g.png?1721288796)


Lear More: [How to Enable Employee Leave Modifications for Past Approved Leaves in BrioHR](https://support.briohr.com/knowledge/how-to-enable-employee-leave-modifications-for-past-approved-leaves-in-briohr?hs_preview=HaLZSkgV-174791849789&hsLang=en)


##### 4.5. Set a Limit of Time for Leave to Be Booked in Advance (Advance Notice)


- **Minimum Limit: **Choose** 'Yes, set a limit'** with a limit amount, e.g, 7 days


- - Employees must apply for leave at least seven (7) days in advance.
  - The system will not allow leave to be applied if employees attempt to apply lesser that 7 days' notice.
- **Maximum Limit:  **Choose** 'Yes, set a limit'** with a limit amount, e.g, 1 month.


  - Employees are allowed to apply for leave up to a maximum 1 month in advance





[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343976153/original/--MtyAPBI9S4ZdQzWAvrqA5cJH050IMrvA.png?1721291756)


**Learn More:** [How to Set a Time Limit for Leave Booking in Advance](https://support.briohr.com/knowledge/how-to-set-a-time-limit-for-leave-booking-in-advance?hs_preview=bNvFBqLJ-174748955176&hsLang=en)


##### 4.6. Set a Limit to the Period that can be Booked at a Time (Consecutive Days)


Restrict how many days can be booked in one application.


For example, if you select 3 days, then a leave which duration exceeds 3 days (excluding non-working days) will not be allowed.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343986144/original/KAzy29VWbv7sDnCXlD_CA6gCPBA62hWZ2w.png?1721296249)


**Learn More:** [How to Set a Time Limit for Leave Booking in Advance](https://support.briohr.com/knowledge/how-to-set-a-time-limit-for-leave-booking-in-advance?hs_preview=bNvFBqLJ-174748955176&hsLang=en)


##### 4.7. Leave Balance Reminder


An option to send a notification to all the employees about their leave balance.


Set:


- Frequency of email reminders
- Minimum balance for employees to be included


![3-13](https://support.briohr.com/hs-fs/hubfs/3-13.png?width=670&height=147&name=3-13.png)


##### 4.8. Notification for Leave That Has Been Approved


Add emails to receive notifications each time assigned employees'** leave have been approved.**


This can be a **third-party email address**, such as HR Operations. You can decide to attach a calendar invitation with the email.


**CAUTION:**

**Do not add the managers/approvers' email addresses**. They will, by default will be notified each time their employees apply for leave and require approval.


##### 4.9. Mandatory Attachment/Justification


Require employees to upload** supporting documents **or add a** justification message **before submitting their request.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48343990194/original/hUDXm3Pp4haZYyxlJK3PvZUQDxSwjxZBkQ.png?1721298187)


**4.10. Custom fields**


Collect additional information during leave application. Field types include:


- Text
- Number
- Date
- Dropdown (Select)  from


![3-15](https://support.briohr.com/hs-fs/hubfs/3-15.png?width=670&height=113&name=3-15.png)


Once all the configurations have been set up, do not forget to click** Save Settings **to ensure all modifications are captured.


---


### Step-by-Step Guide: Configure a Leave Policy (Custom Configuration)


Use this section when certain employees require exceptions such as:


- Different entitlement
- Special approvers
- Different proration mode
- Custom carry-forward
- Custom advance notice rules


Click on a customization type to start the process. For any customization, you will follow the same process:


- Select the employee(s) to customize and click next.
- Choose the value or setting you would like to apply to them.
- Check the impact of your customization and approve.


**NOTE:**


The custom configuration made to an employee will supersede the setting of general configuration


**CAUTION:**

If you change an employee's leave policy, all custom configurations applied to them will be removed.


**Learn More:**


- [How to Set Up Custom Leave Configuration in BrioHR Leave Policies](/knowledge/how-to-set-up-custom-leave-configuration-in-hr-lounge?hsLang=en)
- [How to Customize Leave Approvers for Employees in BrioHR Leave Policies](/knowledge/how-to-customize-leave-approvers-for-employees?hsLang=en)








**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


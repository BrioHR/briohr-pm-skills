---
title: "How to Set Up Shift Premiums and Deductions in BrioHR Time Attendance"
category: "Time Attendance"
subcategory: "Time Attendance Configuration"
source_url: "https://support.briohr.com/knowledge/setup-shift-premiums-and-deductions-in-briohr"
date: "January 6, 2026"
---

# How to Set Up Shift Premiums and Deductions in BrioHR Time Attendance

*Learn how to configure Shift Premiums and Deductions in BrioHR Time Attendance to automate payroll calculations based on attendance, lateness, and shift behavior.*

### Introduction


Shift Premiums and Deductions in BrioHR is a feature that automates payroll calculations based on employee's real attendance and shift behaviour.


For example:


- Employees with **no lateness or early clock-outs** in a monthly timesheet may receive a **Meal Allowance** (premium payment).
- Employees with **lateness records** may receive a **Lateness Deduction**.


**IMPORTANT NOTE:**


The shift premiums and deductions are currently available for work schedule with **shifts arrangement** only.


---


### Part A: Setting Up Tag, Shift, and Work Schedule Assignment


Before configuring premiums and deductions, ensure that you have:


- Created a tag and assigned it to the shift.


  - Learn [how to create a tag](https://support.briohr.com/knowledge/how-to-create-tag-location-activity-and-workstation-for-work-shift?hsLang=en)
  - Learn [how to create a new work shift and assign a tag](https://support.briohr.com/knowledge/how-to-create-new-work-shifts?hsLang=en)
- Set up a work schedule for employees.

  - Learn [how to setup work schedule with shifts](https://support.briohr.com/knowledge/how-to-create-a-work-schedule-with-shifts?hsLang=en)
  - Learn how to assign a work schedule [by offices](https://support.briohr.com/knowledge/assign-work-schedules-by-office-briohr?hsLang=en), or [custom assign to employees](https://support.briohr.com/knowledge/how-to-assign-work-schedule-by-employee?hsLang=en)


---


### Part B: Payroll Custom Pay Items


Shift premiums and deductions must be linked to **Custom Pay Items** in Payroll. These items must be set with unit types:


- **Shift**
- **Hours**


Learn more: [How to Create Custom Pay Items in BrioHR](https://support.briohr.com/knowledge/how-to-create-a-custom-pay-item-in-briohr?hsLang=en)


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-25-2025-08-57-12-1342-AM.png?width=546&height=220&name=image-png-Aug-25-2025-08-57-12-1342-AM.png)


[Embedded content](https://www.loom.com/embed/fbd9b256af894c548e018a7b274adc33?sid=6909cccf-4006-44c4-929a-e9ea48efea9a)


---


### Part C(i): Setting Up Shift Premiums and Deductions


#### Step 1 – Access Shift Premiums & Deductions


1. Go to **HR Lounge > Time Attendance**
2. Click **Policy**
3. Select **Shift Premiums & Deductions**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-25-2025-09-20-26-5539-AM.png?width=670&height=260&name=image-png-Aug-25-2025-09-20-26-5539-AM.png)
**


#### Step 2 – Create Shift Premiums (Extra Pay)


Shift premiums are **extra payments** for meeting specific shift conditions, such as:


- Working night shifts
- Meal allowance eligibility


**Steps to create a premium:**


1. Click **+Create Premium**
2. Fill in the **General Information**:


  - Premium name
  - Shift tag
  - Unit type
  - Eligibility criteria
3. Under **Payroll Connection**:


  - Choose a payroll item for each payroll center
  - Select the pay item created in **Part B**


#### Step 3 – Create Shift Deductions (Penalties)


Shift deductions apply when employees fail to meet expectations, such as:


- Lateness
- Early clock-out


**Steps to create a deduction:**


1. Click **+Create Deduction**
2. Fill in the **General Information**:


  - Deduction name
  - Shift tag
  - Unit type
  - Eligibility criteria
3. Under **Payroll Connection**:


  - Choose a payroll item for each payroll center
  - Select the pay item created in **Part B**


**You can link to multiple tags in one Shift Premium and Deduction creation**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-26-2025-03-06-36-5666-AM.png?width=670&height=263&name=image-png-Aug-26-2025-03-06-36-5666-AM.png)


**The employee's shift behaviour must fit both eligibility criteria to be eligible for  premium and deduction.**


For example:


Employee's shift on 1st August 2025 has both lateness **and** early clocked out. He is eligible for lateness deduction


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-26-2025-03-45-14-6631-AM.png?width=670&height=380&name=image-png-Aug-26-2025-03-45-14-6631-AM.png)





[Embedded content](https://www.loom.com/embed/bf257ebf4bf84dc7bbad5e00df3e8f6c?sid=10a8b9a1-a17f-48a7-8f68-3631b5e9b958)


---


### Part C(ii): Assigning Shift Premiums and Deductions in the Policy


1. Select the **Time Attendance Policy** to modify.
2. Go to **Shift Premiums & Deductions**.
3. To add premiums:


  - Click **Choose/Modify**
  - Select from the list of predefined Shift Premiums
  - Click **Confirm Selection**
4. Repeat the same process for **Shift Deductions**.


[Embedded content](https://www.loom.com/embed/ab8d0ea4e3064911a1886c8fc8c92f22?sid=c5079da9-5a74-482c-8750-3b3214018608)


---


### How Shift Premiums and Deductions Appear in Timesheet


- If an employee is assigned to a policy with premiums/deductions, the system **auto-detects** applicable payments or deductions.
- These appear at the **bottom-left corner** of the monthly timesheet.
- The timesheet captures **units only** (e.g., hours/shifts).
- Actual payment/deduction amounts are applied **after sending the approved timesheet to payroll**.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-26-2025-03-47-44-3311-AM.png?width=670&height=287&name=image-png-Aug-26-2025-03-47-44-3311-AM.png)


---


### How Shift Premiums and Deductions Appear in Payroll


Before sending timesheets to payroll, make sure:


1. The timesheet has been approved by the Manager/HR.


- Learn [how to approve timesheets as a HR](https://support.briohr.com/knowledge/hr-approve-employees-timesheets-time-attendance?hsLang=en).


2. Once approved, send the timesheet to Payroll.


- Lean [how to send approved employees' timesheets to Payroll as a HR](https://support.briohr.com/knowledge/how-to-send-approved-employees-timesheets-to-payroll-in-briohr?hsLang=en)


In Payroll, the system automatically captures:


- Relevant **premium payments.**
- Relevant **deductions.**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-26-2025-04-59-02-2303-AM.png?width=670&height=307&name=image-png-Aug-26-2025-04-59-02-2303-AM.png)
**


Amounts are calculated based on:


- The **unit type settings **(Shift/Hours)
- The **number of shifts/hours** recorded in the timesheet.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-26-2025-04-59-35-1245-AM.png?width=670&height=282&name=image-png-Aug-26-2025-04-59-35-1245-AM.png)


---


#### Frequently Asked Questions (FAQ)


**Q1: Can I apply both a premium and a deduction for the same in a month?**


**A: **Yes, if the employee meets both eligibility criteria (e.g, meal allowance for no lateness, but a deduction for early clock-out).


**Q2: Can I link multiple payroll centers to the same premium/deduction?**


**A:** Yes, you can assign different payroll items for each payroll center.


**Q3: Will deductions apply retroactively if I update the time attendance policy?**


**A:** No, deductions and premiums apply from the point of update onward. Past approved timesheets remain unchanged.


**Q4: Where can I check the final calculated amount?**


**A:** The final calculation is visible in Payroll after the approved timesheet is set from Time Attendance.





**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


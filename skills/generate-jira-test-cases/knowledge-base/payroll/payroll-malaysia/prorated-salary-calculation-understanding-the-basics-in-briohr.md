---
title: "Prorated Salary Calculation: Understanding the Basics in brioHR"
category: "Payroll"
subcategory: "Payroll - Malaysia"
source_url: "https://support.briohr.com/knowledge/prorated-salary-calculation-understanding-the-basics-in-briohr"
date: "August 11, 2026"
---

# Prorated Salary Calculation: Understanding the Basics in brioHR

*Learn how to calculate prorated salaries using brioHR's formulas for Malaysia Payroll. Explore detailed examples and understand the impact of different calculation bases like fixed days, working days, and all days in the current month.*

**Audience & Scope**


Audience: HR Admin


Module: Payroll


Country: Global


Pre-requisites: Payroll Manager access to required payroll center





In brioHR, there are three formulas to calculate the basis of prorated salary:


1. Fixed Number of Days
2. Working Days in the Current Calendar Month
3. All Days in the Current Calendar Month


Understanding how the **daily rate** is calculated for each formula is crucial.


If you're looking for instructions on how to set up the basis of prorated salary calculation, please refer [here](https://support.briohr.com/knowledge/how-to-set-up-company-payroll-general-settings-in-malaysia?hsLang=en).





#### 1. Fixed Number of Days (Working Days Based on Work Schedule)


**Formula:**


Salary / (Number of fixed days set in the system) = **Daily Rate**


Daily Rate x Number of working days in the month = **Prorated Salary**


**Example:**


- Salary: RM 3000
- Prorated Fixed Days set in the system: 26
- Join Date: 11 September 2023
- Number of Days Employee Worked: 15 days (excluding weekends)


**Calculation:**


**RM 3000 / 26 **= RM 115.38 **(Daily Rate)**
RM 115.38 x 15 days worked = **RM 1,730.77** **(Prorated Salary)**





#### 1.1 Salary Proration due to Salary Change mid-month


When an employee’s salary changes effective mid-month, the payroll will automatically prorate the salary based on the applicable salary rates for each period within the month.


For example, if the salary change is effective **15 July**, the employee’s salary will be calculated based on the **previous salary rate from 1–14 July**, and the **new salary rate will be prorated from 15–31 July**. When payroll is processed this amount will be automatically captured.


**Example of system calculation using Fixed Number of Days setting:**


Employee has a salary increment of RM 7500 effective 15th July.


Fixed Working days in July 2026 = **26 Days (based on configurations)**

i) Employee salary from **1st July to 14th July (10 days)**= **RM6000 (old salary)**


RM6000 / 26 = RM230.77


RM230.77 x 10 Days** = *RM 2307.7***


ii) Employee salary from **15th July to 31st July (13 days)**= **RM7500 (new salary)**


RM7500 / 26 = RM288.46


RM288.46 x 13 Days** = *RM 3749.98***


**Prorated salary for July **= RM2307.7 + RM3749.98** = RM6057.68**


**NOTE:**


The system calculates an employee's number of working days based on the "**working days**" set in the Work Schedule. If you select 5 days (e.g., Mon - Fri), the system excludes unselected days.


To access the Work Schedules, click into **Settings > Schedules & Shift > Work Schedule**. You can then assign employees to their respective schedules.


**Public holidays will be captured as working days using this setting.**


####


####


#### 2. Working Days in the Current Calendar Month (Excluding Weekends)


**Formula:**


Salary / (Total days in the month - Total weekends in the month) = **Daily Rate**
Daily Rate x Number of days worked in the month = **Prorated Salary**


**Example:**


- Salary: RM 3000
- Join Date: 11 September 2023
- Working Days in September 2023: 21 days
- Number of Days Employee Worked: 15 days (excluding weekends)


**Calculation:**


**RM 3000 / 21 working days** = RM 142.86 **(Daily Rate)**
RM 142.86 x 15 days worked = **RM 2,142.86** **(Prorated Salary)**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292893833/original/eA30O3quP4QIk7TeCjvylNjAv7zG3EG9xA.png?1681697080)





#### 2.1 Salary Proration due to Salary Change mid-month


When an employee’s salary changes effective mid-month, the payroll will automatically prorate the salary based on the applicable salary rates for each period within the month.


For example, if the salary change is effective **15 July**, the employee’s salary will be calculated based on the **previous salary rate from 1–14 July**, and the **new salary rate will be prorated from 15–31 July**. When payroll is processed this amount will be automatically captured.


**Example of system calculation using Working Days in the Current Calendar Month setting:**


Employee has a salary increment of RM 7500 effective 15th July.


Working days in July 2026 = **23 Days** (excluding weekends)

i) Employee salary from **1st July to 14th July (10 days)**= **RM6000 (old salary)**


RM6000 / 23 = RM 260.87


RM 260.87 x 10 Days** = *RM 2608.7***


ii) Employee salary from **15th July to 31st July (13 days)**= **RM7500 (new salary)**


RM7500 / 23 = RM 326.09


RM 326.09 x 13 Days** = *RM 4239.17***


**Prorated salary for July **= RM 2608.7 + RM 4239.17** = RM 6847.87**


**NOTE:**


The system calculates the number of working days based on the "**working days**" set in the Work Schedules. This formula is applied only when 'Working Days in the Current Calendar Month' is selected as the basis for prorated salary calculation.

**Public holidays will be captured as working days using this setting.**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48323782443/original/lCks0QECY6oh7lT0rR13BdRdRcYXDw24Ag.png?1705456100)


####


#### 3. All Days in the Current Calendar Month (Including Weekends)


**Formula:**


Salary / (All days in the calendar month) = **Daily Rate**
Daily Rate x Number of days worked in the month = **Prorated Salary**


**Example:**


- Salary: RM 3000
- Join Date: 11 September 2023
- Total Days in September 2023: 30 days
- Number of Days Employee Worked: 20 days (including weekends)


**Calculation:**

**RM 3000 / 30 days** = RM 100.00 **(Daily Rate)**
RM 100.00 x 20 days worked = **RM 2,000.00 (Prorated Salary)**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292893905/original/0QDHiKO_W0GhSk_dPIo7OSjRmIfTu_bpag.png?1681697162)





#### 3.1 Salary Proration due to Salary Change mid-month


When an employee’s salary changes effective mid-month, the payroll will automatically prorate the salary based on the applicable salary rates for each period within the month.


For example, if the salary change is effective **15 July**, the employee’s salary will be calculated based on the **previous salary rate from 1–14 July**, and the **new salary rate will be prorated from 15–31 July**. When payroll is processed this amount will be automatically captured.


**Example of system calculation using All Days in the Current Calendar Month setting:**


Employee has a salary increment of RM 7500 effective 15th July.


Working days in July 2026 = **31 Days**

i) Employee salary from **1st July to 14th July (14 days)**= **RM6000 (old salary)**


RM6000 / 31 = RM 193.55


RM 193.55 x 14 Days** = *RM  2709.7***


ii) Employee salary from **15th July to 31st July (17 days)**= **RM7500 (new salary)**


RM7500 / 31 = RM 241.94


RM 241.94 x 17 Days** = *RM 4112.98***


**Prorated salary for July **= RM 2709.7 + RM 4112.98 ** = RM 6822.68**





**Ownership**


Last updated by : Arveena


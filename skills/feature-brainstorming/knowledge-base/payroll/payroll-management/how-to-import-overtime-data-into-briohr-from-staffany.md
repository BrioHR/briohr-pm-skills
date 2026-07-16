---
title: "How to Import Overtime Data into BrioHR from StaffAny"
category: "Payroll"
subcategory: "Payroll Management"
source_url: "https://support.briohr.com/knowledge/how-to-import-overtime-data-into-briohr-from-staffany"
date: "July 12, 2026"
---

# How to Import Overtime Data into BrioHR from StaffAny

*This article explains how to import overtime data from StaffAny into BrioHR payroll using the integration.*

Wouldn't it be great if you could reduce manual work and increase accuracy when processing payroll for employee overtime? With BrioHR and StaffAny, you can do just that! This guide provides a simple overview of the integration process.


[[WATCH THIS VIDEO](https://www.loom.com/share/64b30dd1f0744a21a32ef777c7be01f7?sid=f808ed73-a53c-4aa1-8d9c-5bb4708ad3c3)] - **Learn how to effortlessly import data from StaffAny into BrioHR.**





[Embedded content](https://www.loom.com/embed/64b30dd1f0744a21a32ef777c7be01f7?sid=515896a9-fb6e-42c0-8a32-2806e5150b4d)


---


#### What This Guide Covers:


- Payroll Calculation Rules
- Configuring Employee Information in BrioHR and StaffAny
- Setting Up Company Policies in StaffAny
- Exporting Timesheets for Payroll Processing from StaffAny
- Consolidating Timesheet Data Using Integration Excel
- Exporting the File to Run Payroll in BrioHR
- Common Questions
- Common Errors


---


### 1. Payroll Calculation Rules


This section summarizes the payroll calculation rules integrated between StaffAny and BrioHR.


![cB5OlLuRa_3EkdMKdY6dHDOHXI6EUCLRyA.png?1690269892](https://support.briohr.com/hs-fs/hubfs/Imported%20images/cB5OlLuRa_3EkdMKdY6dHDOHXI6EUCLRyA.png%3F1690269892.png?width=650&height=615&name=cB5OlLuRa_3EkdMKdY6dHDOHXI6EUCLRyA.png%3F1690269892.png)


**NOTE:**


**StaffAny provides the timesheet hours, while BrioHR provides the rates/wages.**


---


### 2. Configuring Employee Information in BrioHR and StaffAny


To ensure successful payroll integration, employee information between BrioHR and StaffAny must match.


#### 1. Employee Name & Employee ID


**A. BrioHR:**


- Go to **People **> Select **Employee **> Click **Edit**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305553094/original/uVvAozhcln_nR6DaJruPOmSOWMi0LDJlng.png?1690270321)


**B. StaffAny:**


- Go to My T**eam > Select Employee **> Input Name under **Basic Information**, Employee ID under **Work Information**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305553444/original/RRjsWEt8YGosYAP18NHc_xe9ahZXjiWRLg.png?1690270486)


#### 2. Salary


This table shows the mapping of salary types between StaffAny and BrioHR.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305553673/original/S6akk-_tJhRj7H4bXdIQhPwaz5YbTxt0jw.png?1690270635)


**A. BrioHR:**


- Go to **People > Select Employee** > Click **Compensation **> **Salary > Edit.**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305554545/original/6YZhzVQM87iGH8y9k2kwFsefDvEXNUEFvQ.png?1690270998)


**B. StaffAny:**


- Go to **My Team** > Select **Employee **> **Wages**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305554864/original/XMhgaGtvwGJQ8QEFnVvUmnmTX2hkUICDbw.png?1690271131)


---


### 3. Setting Up Company Policies in StaffAny


If your company has different policies for Rest Days, Public Holidays, Weekends, or Overtime, configure your settings accordingly in StaffAny.


#### Setting Up Rest Days


- Go to **Settings **in StaffAny.
- Click on the **Shift Tag** tab.
- Click on **Add Tag**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305555337/original/SeL-sf1qoFjHyw3ngqJwKOOwOLrcNnWgcQ.png?1690271336)


- Choose **Rest Day/Off Day.**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305555512/original/jqr0TMnSCQGvz5Sz4OkhShuSmu2PedHtAg.png?1690271420)


- **Do not modify anything**. Click **Save**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305555716/original/r1ZG2HWQQfRFNE9IVAgrxZIk8b7ojiHvuw.png?1690271503)


- Apply the shift tag to employees who work on Rest Days by doing [this](https://help.staffany.com/en/articles/5789474-rest-day-work-automated-tagging).


**Setting Up Weekends, Public Holidays, and Overtime**


Similarly, configure your settings for **Weekends, Public Holidays**, and **Overtime**.


---


### 4. Exporting Timesheets for Payroll Processing from StaffAny


**NOTE:**


**Before transforming your timesheet for importing, we strongly advise locking your timesheets before processing payroll. [Read more about timesheet locking](https://help.staffany.com/en/articles/4871108-timesheet-lock).**


- Select the date range for the payroll period.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305557214/original/-ARbtxHh-bkMdd-WC0tvX7TC-LYuFZG1vw.png?1690272218)


- Under **Export Filtered**, click **Individual **to generate the Detailed Timesheet report.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305557553/original/rWuAO5F0fNI3wwwGptJbi62dW7GXMTpgFg.png?1690272387)


- The Timesheet CSV file will be downloaded to your device.


---


### 5. Consolidating Timesheet Data Using Integration Excel


**NOTE:**


**Before transforming your timesheet for importing, we strongly advise locking your timesheets before processing payroll. [Read more about timesheet locking](https://help.staffany.com/en/articles/4871108-timesheet-lock).**


1. **Make a copy of the BrioHR Timesheet template by signing into your Google account.**

  1. Contact the StaffAny team to obtain a copy of the BrioHR Timesheet Template.
2. **Set up Optional Configuration Rules:**

  1. **Lateness Tiering:** Accumulates total late minutes per employee, categorizing them into tiers.


![YtY_2GEqwUtyQXFVDqb9f_1J2hc9rSzRZw.png?1690272651](https://support.briohr.com/hs-fs/hubfs/Imported%20images/YtY_2GEqwUtyQXFVDqb9f_1J2hc9rSzRZw.png%3F1690272651.png?width=604&height=320&name=YtY_2GEqwUtyQXFVDqb9f_1J2hc9rSzRZw.png%3F1690272651.png)


**NOTE:**


**Customize the name, range, and points as needed.**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305558166/original/iYw6c7XzOm7jro6RShZ3pcl0yfTxJtvySg.png?1690272680)


Set penalties based on points after configuration.


- **Unpaid Leave Days:**


![_2mXkCM7JLVvFYsCEXS237uxLbWGyZRtjA.png?1690272753](https://support.briohr.com/hs-fs/hubfs/Imported%20images/_2mXkCM7JLVvFYsCEXS237uxLbWGyZRtjA.png%3F1690272753.png?width=520&height=236&name=_2mXkCM7JLVvFYsCEXS237uxLbWGyZRtjA.png%3F1690272753.png)


Specify unpaid leave types by adding the leave tag and corresponding leave name in the “Off and Leave” settings.


3.   **Copy and paste the timesheet data into the Integration Excel:**


a. Open the downloaded Timesheets Individual CSV file.


b. Inside the copied "**Import - TS Individual**" tab, clear the spreadsheet.


**i**. Ctrl-A + backspace


c. Copy the data from the timesheet file and paste it into the "**Import - TS Individual**" tab on Google Sheets.


d. Wait for the small blue loading bar (top right corner) to finish loading.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305558917/original/6-GPmtMlBwy9FsUUoejCUz5MiLJR-8CszQ.png?1690273013)


e. Review the summarized timesheets in the "Output - Summary" tab.


f.  Download the “Output - BrioHR Template” sheet as a CSV.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305559234/original/7C716I61CAX2EJ6Go463qoG4rWE9xe_Tmw.png?1690273123)


---


### 6. Exporting the File to Run Payroll in BrioHR


- In BrioHR, go to **HR Lounge > Payroll**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305560128/original/Hh8IM_ae83utNcii60jIf30BhAOqCqOaSg.png?1690273558)


- Click on **Run Payroll**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305560280/original/YxhOEk0scq1hOBvkkFaWL8SqgLwmNIBYgw.png?1690273629)


- Click **Add items in Bulk**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305560363/original/sbEHtMumzOvJpyV09f0MY9JsIg7b2vQDZQ.png?1690273667)


- Choose the following:

  - Select Type: **Addition**
  - Addition Type: **Overtime (Multi-rates)**
  - Click **Import Overtime**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305560502/original/uJqtOR7rtNIm2CeLvCcyCTo3T4ovVpcUZQ.png?1690273747)


- Under Select File Source, choose **StaffAny File**.
- Upload the file from your computer and click **Upload**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305560649/original/PW-Y9l3WplD504qjDfq_HXqAdugbFc3OUA.png?1690273825)


- The timesheet data will be successfully uploaded.
- Review and verify the imported payroll data.
- Once confirmed, proceed to run the payroll process.


---


### 7. Common Questions


#### Will leave data from StaffAny sync with BrioHR?


**No, leave data in StaffAny is not synced with BrioHR.**


We advise managing leave separately in StaffAny.


Learn more about StaffAny Leave Management [here](https://help.staffany.com/en/articles/3589849-leave-setup-managing-leave-balance-leave-migration).


---


### 8. Common Errors


#### Employee ID mismatch


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48305561146/original/mWZpw8aR_mankYjTwj-HghkcUSwJtejElA.png?1690274033)


**This error indicates that some Employee IDs differ between StaffAny and BrioHR.**


For successful payroll integration, ensure employee information matches between the two systems. Refer to "**Configuring Employee Information in BrioHR and StaffAny**" for more details.








**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


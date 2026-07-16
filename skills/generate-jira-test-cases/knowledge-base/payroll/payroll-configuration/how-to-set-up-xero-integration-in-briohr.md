---
title: "How to Set Up Xero Integration in BrioHR"
category: "Payroll"
subcategory: "Payroll Configuration"
source_url: "https://support.briohr.com/knowledge/how-to-set-up-xero-integration-in-briohr"
date: "July 12, 2026"
---

# How to Set Up Xero Integration in BrioHR

*This article explains how to set up the Xero integration to generate accounting entries from BrioHR payroll, including account mapping configuration.*

### A. Introduction


BrioHR offers seamless one-click integration with Xero, an accounting solution that allows companies to generate accounting entries in Xero based on payroll calculations completed in BrioHR. This guide is designed for accountants, finance professionals, and HR managers responsible for payroll management. It will walk you through configuring account mappings in BrioHR to ensure accurate payroll data transfer to Xero.


#### How the Integration Works


- **Log in to Xero:** Start by logging into your Xero account from BrioHR. This step enables you to retrieve account names from Xero and facilitates data transfer from BrioHR to Xero.
- **Configure Account Mapping**: Set up your account mapping in BrioHR to ensure that accounting entries are created in the correct Xero accounts.
- **Process Payroll and Transfer:** After running payroll, click “Transfer to Xero.” This action creates a draft journal entry in Xero. You can review, edit, or delete this draft before posting it from your Xero account.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Mar-09-2026-03-58-07-2212-AM.png?width=670&height=238&name=image-png-Mar-09-2026-03-58-07-2212-AM.png)


### B. Connecting To Xero From BrioHR


- Navigate to the **HR Lounge** (top menu), select "**Payroll**," and then choose "**Xero**."
- Click the “**Connect**” button, enter your Xero account details, and authorize BrioHR to establish the connection.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48217567933/original/HBaG5Xthk9KWlV6_8IHvV4u4IsKGFehMbQ.png?1650357750)


### C. Account Mapping


Begin by selecting the following:


- **Xero Organization: **Choose **your Xero organization** from the list.
- **Grouping:** Select the appropriate **grouping **option:
- **Company:** For payroll accounting entries grouped at the company level.
- **Office:** For grouping entries at the office level, useful if you have multiple branches or outlets.
- **Department:** For grouping entries at the department level. Most companies opt for the “**Company**” setting.
- **Salary Mapping:** Choose between:

  - **Basic Salary:** If you prefer to map basic salaries first, allowing you to separate expenses such as allowances into different accounts.
  - **Net Salary:** If you want to map net salaries first. Refer to the “Mapping Example” section for more details.


After making these selections, proceed with account mapping. For each payroll item, select the corresponding debit and credit accounts in Xero according to your accounting preferences.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48217570491/original/UAFarpVC1d_jT4pU8d-V_ScORNkS26zlPg.png?1650357927)


**WARNING:**


**If you use the “Basic Salary” mode, you must map all payroll items used in your payroll, excluding basic salary and statutory contributions. This includes allowances, bonuses, deductions, unpaid leave, etc. Use the “Add Payroll Item” button for this purpose.**


![fcdMRa88X0Urr62V9trGHj74rCsQ8QbtUw.png?1650357987](https://support.briohr.com/hs-fs/hubfs/Imported%20images/fcdMRa88X0Urr62V9trGHj74rCsQ8QbtUw.png%3F1650357987.png?width=670&height=104&name=fcdMRa88X0Urr62V9trGHj74rCsQ8QbtUw.png%3F1650357987.png)


### D. Mapping Example


- Many clients use a mapping approach similar to the one described below. The goal is to differentiate between basic salary and other items such as allowances while grouping liabilities to employees and statutory bodies.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48217572524/original/OcuOYJ-mX2d3hpfMk6wjXvQr4dKniUHCnQ.png?1650358059)


- Refer to the mapping example for a detailed breakdown. After configuring, remember to save your settings by clicking the "**Save**" button at the bottom right.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48217572761/original/WuGzpeH9J1uYTKzWMDJttjb5VCV9mSqN2g.png?1650358093)


### E. Transferring Data To Xero


After completing your configuration and processing payroll for a specific month, you can create a manual journal entry in Xero.


- Go to **HR Lounge > Payroll** and select a “**Completed**” month from the main dashboard. Scroll down to find the Xero section.
- Click “**Preview**” to see a summary of the amounts mapped from your payroll run into the correct Xero accounts.


**WARNING:**


**Double-check all amounts to ensure that all payroll items used in the payroll run are accurately mapped. Any discrepancies indicate incorrect mapping.**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48217574037/original/XaTi68aKb6Po4iImXmN2LZHlEPzXN-7VzA.png?1650358187)


Once verified, click “**Transfer**” to finalize. You will find a **draft manual journal** in Xero as shown in the sample below.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48217574455/original/t0VbC3YWdPbPnHTgXd-gEHzCtwHVvDiTvQ.png?1650358221)


---


### FAQ


**Q1: How do I disconnect from Xero?**


A1: We provide a **Disconnect** button within the Xero integration page to disconnect Xero integration


**Q2: What doesn’t your integration do?**


A2: At this time, we only support the creation of manual journal entries.


**Q3: When and how does data sync occur?**


A3: It is **not real-time**. Sync is action-based:


- Organization/chart of account fetch after connect/organization mapping
- Chart of accounts refresh via the **Refresh Accounts** button
- Accounting entries transfer when the user triggers the transfer flow


**Q4: Why is the Disconnect button disabled?**


A4: It is disabled until an **organization mapping** exists.


**Q5: What data is sent to Xero?**


A5: Accounting entries are sent as **Manual Journals** (draft status) with mapped account lines.





**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


---
title: "How to Process a Payroll Parallel Run in BrioHR (Malaysia Payroll Guide)"
category: "Implementation with BrioHR"
subcategory: "General"
source_url: "https://support.briohr.com/knowledge/how-to-process-a-payroll-parallel-run-in-briohr-malaysia-payroll-guide"
date: "August 24, 2025"
---

# How to Process a Payroll Parallel Run in BrioHR (Malaysia Payroll Guide)

*Learn how to run a payroll parallel test in BrioHR for Malaysia payroll. Step-by-step guide to ensure EPF, SOCSO, EIS, and PCB accuracy before going live.*

If you're new to **BrioHR's Payroll module**, running a **payroll parallel run** is a key step to ensure your transition is smooth and accurate. This typically happens **one month before** **your official go-live**.
By this stage, our migration team would have uploaded your payroll data for the current year to date (e.g., January to March), and you’ll process a **parallel run** for the most recent payroll month — usually the current or previous month — directly in Brio.


The purpose of this parallel run is to simulate a full payroll cycle in Brio using data from a month you’ve already processed in your previous payroll system. You’ll then compare Brio’s results against your existing payroll reports to identify and fix any discrepancies before going live.


This guide walks you through how to run the payroll parallel process step-by-step.


### Step 1: Process Payroll in BrioHR


1. Go to the **Payroll** module and process payroll as usual.
2. Add any applicable additional pay items that may apply for the month.


  - **Tip**: Hover over the home icon next to the pay item to check if statutory contributions (EPF, SOCSO, EIS, PCB, etc.) are set correctly.

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-43-22-1823-AM.png?width=688&height=343&name=image-png-Jul-22-2025-03-43-22-1823-AM.png)
  - If the contributions differ from what you expect, verify and update the pay item settings using this guide: [How to Create a Custom Pay Item](https://support.briohr.com/knowledge/how-to-create-a-custom-pay-item-in-briohr?hsLang=en).
3. Compare the payroll results in BrioHR against your current payroll system.


  - Check key figures like EPF, SOCSO, EIS, PCB, employer contributions, and net salary.
4. If there are discrepancies, proceed to Step 2 — **but keep the payroll tab open** so you can refresh and recalculate after making changes.


### Step 2: Review Statutory Settings


1. Open a new tab and go to **Employee Profile > Payroll** tab.

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-47-01-9326-AM.png?width=688&height=341&name=image-png-Jul-22-2025-03-47-01-9326-AM.png)
2. Confirm statutory configurations like:


  - Tax residency
  - Marital status
  - Number of children / dependents
  - PCB category
  - EPF Contribution
  - SOCSO & EIS
3. If you make any changes, return to the payroll run and click the **refresh** icon in the payroll tab to recalculate the figures.

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-51-10-5116-AM.png?width=688&height=301&name=image-png-Jul-22-2025-03-51-10-5116-AM.png)
4. If the difference still exists, continue to Step 3.


### Step 3:


1. Open another new tab and go to **Report Builder > Employee Payroll**.
2. Search for the employee’s name, select the payroll center, and set the **month range** to cover all migrated months (e.g., Jan–Mar if you're running April).


You'll see past payroll amounts — total remuneration, employer/employee deductions, and net pay.


- This should match what was migrated into Brio.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-52-23-0827-AM.png?width=688&height=343&name=image-png-Jul-22-2025-03-52-23-0827-AM.png)


### Step 3A: If There Are Differences in PCB


Check the employee's statutory settings again (marital status, tax resident, children, etc.). Make sure the accumulated amounts entered into the calculator match what’s in Brio. Also confirm if any pay items are incorrectly flagged for PCB contribution. Correct these and refresh the payroll.


Go to [LHDN PCB Calculator 2025](https://calcpcbplus.hasil.gov.my/HITS_CE/).


- Choose **"Previously employed in the current year"**.
- Input the current processing month (e.g., April).
- Fill in:


  - Accumulated remuneration
  - Accumulated MTD (PCB)
  - Other deductions
  - Current month’s remuneration
- Generate the result and compare with Brio’s.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-53-27-1477-AM.png?width=688&height=315&name=image-png-Jul-22-2025-03-53-27-1477-AM.png)


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-54-48-7883-AM.png?width=688&height=234&name=image-png-Jul-22-2025-03-54-48-7883-AM.png)


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-55-29-5846-AM.png?width=688&height=426&name=image-png-Jul-22-2025-03-55-29-5846-AM.png)


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-22-2025-03-55-51-9382-AM.png?width=688&height=137&name=image-png-Jul-22-2025-03-55-51-9382-AM.png)


If the result differs, double-check the settings for all pay items involved:


- - Go back to **Settings > Pay Items**, click the pencil icon to edit.
  - Ensure the statutory contribution settings are correct. Refer to the same guide: [How to Create a Custom Pay Item](https://support.briohr.com/knowledge/how-to-create-a-custom-pay-item-in-briohr?hsLang=en).


### Step 3B: If There Are Differences in EPF


Refer to [EPF Jadual Ketiga](https://www.kwsp.gov.my/documents/d/guest/jadual-ketiga-2011-lengkap-bm-pdf?preview) to confirm if the contribution rates are correct. Make sure the relevant pay items are enabled for EPF contributions. You can review and edit pay item settings via [this guide](https://support.briohr.com/knowledge/how-to-create-a-custom-pay-item-in-briohr?hsLang=en).


### Step 3C: If There Are Differences in SOCSO


Check the SOCSO contribution rates using [this reference chart](https://www.perkeso.gov.my/images/dokumen/151124-Rate%20Contribution%20ACT%204.pdf). Similar to EPF, check if the correct pay items are set to contribute to SOCSO.





---


### Final Tips


- Always ensure your pay item settings match statutory expectations (e.g., PCB, EPF enabled, etc.).
- Remember: **Parallel runs are just simulations** — no salaries are paid out.
- Once results align with your existing payroll, you are ready for your **live payroll run in BrioHR.**


If you encounter any issues during the parallel run, please reach out to your assigned **Implementation Manager** for assistance.





**Need Assistance?**

If you have any questions or require assistance, please reach out to our support team via live chat or email us at support@briohr.com.


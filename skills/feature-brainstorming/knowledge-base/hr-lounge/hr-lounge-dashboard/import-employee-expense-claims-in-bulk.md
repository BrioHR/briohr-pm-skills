---
title: "Import Employee Expense Claims in Bulk"
category: "HR Lounge"
subcategory: "HR Lounge Dashboard"
source_url: "https://support.briohr.com/knowledge/import-employee-expense-claims-in-bulk"
date: "July 24, 2026"
---

# Import Employee Expense Claims in Bulk

*This article explains how to efficiently import employee expense claims records in brioHR using the Bulk Import feature. This feature allows Admin users to enter multiple expense claim records via Excel. This process helps ensure efficient data management and consistency, especially for companies with high headcounts.*

**Audience & Scope**


Audience: HR Admin


Module: Employee Management


Country: Global


Pre-requisites: User Group permission to HR Lounge > Employee Management





**Part 1: Enable access for Bulk Import/Export of Expense Claims**


1. Go to **Admin Settings > User Groups > Choose Your User Group**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-15-59-0093-AM.png?width=670&height=256&name=image-png-Jul-24-2026-07-15-59-0093-AM.png)
**


2. Click the **Edit** button


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-16-30-2629-AM.png?width=670&height=310&name=image-png-Jul-24-2026-07-16-30-2629-AM.png)


3. Under **HR Modules Permission**, find **Claim Module**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-17-23-6164-AM.png?width=670&height=539&name=image-png-Jul-24-2026-07-17-23-6164-AM.png)
**


4. Choose the permission option from the '**Allow bulk import of claims reports**' dropdown


You can choose '**Allowed for managed offices**' if you want users in this user group to import claims reports only for employees in their managed offices. Or you can choose '**Allowed for all employees**' if you want users to import claims reports for all employees in the company.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-18-24-0462-AM.png?width=670&height=537&name=image-png-Jul-24-2026-07-18-24-0462-AM.png)


5. Click **Save**





**Part 2: Import Expense Claim Records**


1. Go to **HR Lounge > Employee Management > Bulk Import/Export**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-10-2026-04-30-46-3143-AM.png?width=670&height=295&name=image-png-Jul-10-2026-04-30-46-3143-AM.png)


2. Click the **Claims**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-23-26-0901-AM.png?width=670&height=303&name=image-png-Jul-24-2026-07-23-26-0901-AM.png)


3. **Download** the Claims **template in Green**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-24-05-1682-AM.png?width=670&height=302&name=image-png-Jul-24-2026-07-24-05-1682-AM.png)
**


**NOTE: **


- By default, the downloaded template will contain the list of all claim records currently in the **Approved** status.
- Please DELETE the existing claim records in the Excel and ONLY INCLUDE NEW RECORDS you want to import in the Excel before you upload it.


4. Fill in the necessary details for each employee, including all **required fields** such as:


- Employee email address
- Report (Claim Report Name)
- Claim type
- Transaction date
- Total amount
- Currency


**NOTE:**


- Cash Advance Claim Types are NOT supported.
- Claim type must exist in your claim type list (Expense Claims Module > Claim Types)
- Ensure that all dates and values are entered in the correct format as stated in the template instructions.


A sample of the template is shared below:


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-37-56-6267-AM.png?width=670&height=76&name=image-png-Jul-24-2026-07-37-56-6267-AM.png)


5. Once the information has been filled into the template accurately, save your file and reupload it into the system.


The system will process the data and update the employee claim records according to the **data** provided.


Once the file has been uploaded into the system, check and confirm the information uploaded, and then proceed to click on **Save Import Data**.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-24-2026-07-42-54-5618-AM.png?width=670&height=184&name=image-png-Jul-24-2026-07-42-54-5618-AM.png)


6. Once the data is imported, you will see the pop-up below. The data should reflect accordingly in **Expense Claims > Claims Request** section for the employees you included. You can filter for 'Approved' if needed.


**NOTE: **


All imported claims will be automatically **APPROVED.**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-10-2026-04-52-09-1208-AM.png?width=363&height=301&name=image-png-Jul-10-2026-04-52-09-1208-AM.png)





**Common Issues/FAQ**


**1. Who can access the Bulk Import/Export Claims feature in brioHR?**


Only users with **HR or Admin** access permissions can use the Bulk Import/Export feature. Refer to Part 1 of this article.


**2. Can I edit the imported claim record?**


As the imported claims will automatically be approved, you will need to reopen the individual claim, make your edit, and resubmit it for approval. You can approve the claim on behalf to change the status back to approved. But please note that the employee will receive an email notifying them of the reopening and approval of the claim.


**3. What should I do if the import file shows an error?**


Check for missing required fields, incorrect data formats (transaction date / Column Name), etc. Correct them and reupload the file.


**4. How do I confirm that the claim records have been successfully imported?**


After uploading, the system will show a **confirmation message** or **import summary** indicating the success or failure of the import process. You can check the Expense Claims > Claim Request section to check that the records reflect accordingly. You can also use Analytics > Report Builder > Expense Claims Report to verify the data.


**5. Will the imported claims be counted towards the employee's claim limits and balances?**


Yes, imported claims will also be counted towards the employee's claim limits and balances.





**Related Articles**


[How to Create Expense Claims on Behalf of Other Employees](/knowledge/how-to-create-expense-claims-on-behalf-of-other-employees?hsLang=en)


[How to re-open claim (by HR/Admin)](/knowledge/how-to-re-open-claim?hsLang=en)


[How to approve, reject, reopen, cancel claims in bulk as HR](/knowledge/how-to-approve-reject-reopen-claims-in-bulk-as-hr?hsLang=en)





**Ownership**


By: Aqilah


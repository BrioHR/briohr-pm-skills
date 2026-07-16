---
title: "How to Set and Manage Claim Threshold Amounts for Approval Workflows"
category: "Expense Claims"
subcategory: "Claims Configuration"
source_url: "https://support.briohr.com/knowledge/how-to-set-and-manage-claim-threshold-amounts-for-approval-workflows"
date: "July 12, 2026"
---

# How to Set and Manage Claim Threshold Amounts for Approval Workflows

*This article explains how to set claim threshold amounts in Claim Policies for grouped and non-grouped approval workflows.*

There are two primary methods for setting a claim threshold under **Claim Policies**. Each method applies differently based on the selected settings:


**A. Approval for Non-Grouped Claims/Claim Group:** Applied to the approval workflow for claims that are either non-grouped claims or part of a claim group (based on the selection on the Approval page), and for employees who do not have a custom approval workflow.


**B. Custom Approval Workflow for Employee: **Applied to the approval workflow for claims made by employees who have a custom approval workflow.


---


### New Feature: Threshold at Report Level


Previously, claim thresholds referred to the amount of each individual claim item in a report. Now, you can set the threshold to refer to the total amount of the entire claim report instead. This option can be enabled by selecting the **Threshold Type** when creating the threshold.


- **Transaction Level**: Applies if one or more claim transactions exceed the specified amount.
- **Report Level:** Applies if the total amount of the claim report exceeds the specified amount.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48345841805/original/8WggWOQfEq3IKw4i_uoZqdP2Llq0m1caNQ.png?1722849692)


---


### A. Setting Thresholds for Non-Grouped Claims/Claim Group


1.   In **HR Lounge**, click on **Expense Claims**.


2.   Navigate to Claim Policies and click on the policy name.


3.   Go to **Approval**.


4.   Click the **Edit **button for Non-Grouped Claims/Claim Group.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48337194735/original/wjSX4kOw4YotX7opGDsaHTDL8XBdot4ctQ.png?1715911109)


5.   Click on **+ Create Workflow.**


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48337194961/original/Msx1XWPCkYGsjl6s_IT22FTukfKVRi_2gA.png?1715911430)


6.   To set the threshold for an approver, tick the **Enable Threshold** checkbox.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48345839649/original/yyUV2u8JmhW4puoOLWbrTvwET0TeVXHPkw.png?1722848780)


7.   Select the **Threshold Type:**


- **Transaction Level:** Applies if one or several claim transactions exceed the specified amount.
- **Report Level:** Applies if the total claim report amount exceeds the specified amount.


8.   Enter the **Amount **and select the **Offices**.


**NOTE:**


**To add more than one threshold, click on the + Add Rule icon.**


9.     Fill in all other details such as **Workflow Name** and click the **Create **button.


10.  Select the **approval **workflow and **confirm the selection**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48337196831/original/FfffJD4p6wpJDqUl8xhjVOdGrVwM3LclNw.png?1715914345)


**NOTE:**


**Once a threshold rule is set for an approver, the approval workflow will only apply if the claim exceeds the threshold. Claims below the threshold will be automatically approved without additional approver intervention.**


**Examples:**


- **Transaction Level: If the threshold for the 1st Approver is set at RM 1000:**

  - **Claims where any item exceeds RM 1000 require approval from the 1st Approver.**
  - **Claims where all items are below RM 1000 will either be auto-approved or forwarded to the 2nd Approver (if applicable).**


- **Report Level: If the threshold for the 1st Approver is set at RM 1000:**

  - **Claims where the total report amount exceeds RM 1000 require approval from the 1st Approver.**
  - **Claims where the total amount is below RM 1000 will either be auto-approved or forwarded to the 2nd Approver (if applicable).**


**The threshold applies only to the selected office. For instance, a RM 1000 threshold for Kuala Lumpur will not affect claims from the Johor Bahru office.**


**Ensure that employees are part of the selected office when setting custom thresholds.**


---


### B. Setting Custom Approval Workflow for Employees


1.   In **HR Lounge**, click on** Expense Claims**.


2.   Navigate to **Claim Policies** and click on the policy name.


3.   Go to **Approval**.


4.   Click **+ Create Custom Approval** for Non-Grouped Claims/Claim Group.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48337194693/original/-ubV7CzZ9M3e1xpJR7TUnyO4s5VS9t6wcQ.png?1715911032)


5.   Choose the approver and click **+ Create Threshold**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48337193472/original/C0wwtrTATHXQIv38T7FvibYPUaWjb2cPzw.png?1715909020)


6.   Select the **Threshold Type:**


- **Transaction Level:** Applies if one or several claim transactions exceed the specified amount.
- **Report Level: **Applies if the total claim report amount exceeds the specified amount.


7.   In the pop-up window, enter the **Amount **and select the **Offices**.


**NOTE:**


**To add more than one threshold, click on the + Add Rule icon.**


8.   Click **Save **to complete the action.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48345840016/original/0nv1kB1oA5RIrMP9uLZKqPszADpL0fAuQA.png?1722848928)


**NOTE:**


**Once a threshold rule is set for an approver, the approval workflow will only apply if the claim exceeds the threshold. Claims below the threshold will be automatically approved.**


**Examples:**


- **Transaction Level: If the threshold for the 1st Approver is set at RM 1000:**

  - **Claims where any item exceeds RM 1000 require approval from the 1st Approver.**
  - **Claims where all items are below RM 1000 will either be auto-approved or forwarded to the 2nd Approver (if applicable).**
- **Report Level: If the threshold for the 1st Approver is set at RM 1000:**

  - **Claims where the total report amount exceeds RM 1000 require approval from the 1st Approver.**
  - **Claims where the total amount is below RM 1000 will either be auto-approved or forwarded to the 2nd Approver (if applicable).**


**The threshold applies only to the selected office. For instance, a RM 1000 threshold for Kuala Lumpur will not affect claims from the Johor Bahru office.**


**Ensure that employees are part of the selected office when setting custom thresholds.**


9.   Choose the **employee **to apply the custom approval workflow, tick the checkbox, and click **Apply Customization**.


[](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48337194195/original/CxFiDF23BqRAaQ_Sm8CgKcWHBCkk__O_ng.png?1715910132)


---


### C. What if the Approval Workflow/Threshold Was Set After a Claim Report Was Submitted?


Modifications will not apply to claim reports submitted before the changes were made. To apply the modifications, the claim report must be re-opened and submitted again.


For open or yet-to-be-submitted claim reports, modifications will apply accordingly.








**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


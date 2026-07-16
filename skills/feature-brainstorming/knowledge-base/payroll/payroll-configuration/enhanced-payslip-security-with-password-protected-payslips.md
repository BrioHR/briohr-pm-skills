---
title: "Enhanced Payslip Security with Password-Protected Payslips"
category: "Payroll"
subcategory: "Payroll Configuration"
source_url: "https://support.briohr.com/knowledge/enhance-payslip-security-with-password-protected-payslips"
date: "June 3, 2026"
---

# Enhanced Payslip Security with Password-Protected Payslips

*Protect sensitive payroll data with password-protected payslips sent via email. Learn how to enable this feature, configure password logic, and securely send payslips to employees.*

**Audience & Scope**


Audience: HR Admin


Module: Payroll


Country: Global


Pre-requisites: Admin User group settings enabled, assigned as Payroll Manager





#### Introduction


Safeguarding employee payroll information is a critical responsibility for every organization. To strengthen data security, a new feature has been introduced that enables **password protection for payslips sent via email**. This enhancement ensures that only authorized recipients can access sensitive salary details, adding an extra layer of protection beyond standard system access.


#### What is Password-Protected Payslip?


This feature allows HR teams to send payslips via email as **password-protected PDF files**. Each payslip is secured using a password generated from specific employee data (Date of birth or Identification number), ensuring that only the intended recipient can open and view the document.


#### How the Password Logic Works


The password is automatically generated based on selected employee information. Organizations can choose from identifiers such as:


- Date of Birth
- Identification Number (e.g., NRIC/Foreign Identitfication Number, MyKad, Passport)


To ensure consistency, all identity-based passwords are automatically converted into **capital letters**.


The system applies location-specific logic depending on the payroll center:


- **Malaysia Payroll**

  - Prioritizes **MyKad number**
  - Falls back to **passport number** if MyKad is unavailable
- **Singapore Payroll**

  - Utilizes **Date of Birth**


**IMPORTANT:**


To comply with Singapore regulatory requirements, **"Date of Birth"** must remain the designated password protection method for all Singapore payslip emails.


When this function is enabled for Singapore payroll centers, the setting will appear as per screenshot below:

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jun-03-2026-11-56-01-8939-AM.png?width=740&height=240&name=image-png-Jun-03-2026-11-56-01-8939-AM.png)





#### Step-by-Step Guide to Enable Password Protection


Follow these steps to activate password protection for payslips:


1. **Login to BrioHR**
2. Hover over **HR Lounge** and navigate to the **Payroll module**
3. Select the relevant **Payroll Center**
4. Click on **Settings**, then go to the **General** tab

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Apr-13-2026-03-42-04-8452-AM.png?width=670&height=339&name=image-png-Apr-13-2026-03-42-04-8452-AM.png)
5. Scroll to the **Payslips section** at the bottom of the page
6. Enable the option for **Password Protect Payslip**
7. Choose your preferred **password format****
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Apr-13-2026-03-42-45-4744-AM.png?width=670&height=285&name=image-png-Apr-13-2026-03-42-45-4744-AM.png)
**
8. Click **Save** to apply the changes


**NOTE**:


Screenshots shared in the steps above are for **Malaysian payroll centers** which allow **2 options (Employee Date of Birth or MyKad / Passport Number) **to choose from.


However, for **Singaporean payroll centers**, there is only **1 default option : Date of Birth** as the password.


#### Available Password Formats


You can select from the following password options:


- **Employee Date of Birth**

  - Format: **DDMmmYYYY**
  - Example: *16Nov2002*
- **MyKad / Passport Number**

  - Format: **Last 6 characters (uppercase)**


These formats ensure a balance between security and ease of access for employees.





#### How to Send Payslips via Email


To test or use this feature, follow these steps to send payslips securely:


1. Go to the **Payroll module**
2. Click into the **Completed Payroll Cycle**
3. Navigate to **Send Payslips via Email**
4. Click **Send Payslips**

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Apr-13-2026-03-44-57-4421-AM.png?width=670&height=210&name=image-png-Apr-13-2026-03-44-57-4421-AM.png)
5. Confirm the **Year, Month, and Payroll Cycle**
6. Select employees

  - You can choose **all employees** for bulk sending
  - Or select **multiple employees** as needed
7. Click **Send Payslip**

![image](https://support.briohr.com/hs-fs/hubfs/image-png-Apr-13-2026-03-46-09-6786-AM.png?width=398&height=669&name=image-png-Apr-13-2026-03-46-09-6786-AM.png)





#### Important Notes on Sending Payslips


- If password protection is enabled but required employee information is **missing**, the system will display an **error message** and prevent sending

![image](https://support.briohr.com/hs-fs/hubfs/undefined-Apr-13-2026-03-46-37-3144-AM.png?width=670&height=136&name=undefined-Apr-13-2026-03-46-37-3144-AM.png)
- Once all required information is **updated and complete**, a **success message** will be shown, and the payslips will be sent successfully

![image](https://support.briohr.com/hs-fs/hubfs/undefined-Apr-13-2026-03-46-44-8172-AM.png?width=670&height=193&name=undefined-Apr-13-2026-03-46-44-8172-AM.png)


This ensures accuracy and prevents incomplete or unsecured payslip distribution.





#### Built-in Validation for Accurate Processing


Before sending payslips in bulk, the system performs a validation check:


- If the required employee data for the selected password type is missing, an **error will be triggered**
- The system will **prevent bulk email sending** until all required information is complete


This validation process works similarly to bank file generation, helping to reduce errors and ensure smooth payroll operations.


###


#### Scope of Password Protection


It’s important to understand where this security feature applies:


**Applies to:**


- Payslips sent via email (PDF format)


**Does NOT apply to:**


- Payslips viewed within the system (e.g., employee self-service or admin portal)
- Bulk downloads of payslips by Admin


The system itself already acts as a secure environment, so additional password protection is only required for externally shared documents.





#### Frequently Asked Questions (FAQ)


**Q: Does password protection apply to all payslips?**


A: No, password protection only applies to payslips sent via email as PDF files. Payslips viewed within the system or downloaded in bulk are not password-protected.


**Q: What happens if employee information is incomplete?**


A: The system will display an error message and prevent payslips from being sent until all required employee data is updated.


**Q: Can I choose the password format?**


A: Yes, you can select from available options such as Date of Birth or identification numbers (e.g., MyKad or passport for Malaysia and NRIC or FIN for Singapore).


**Q: What format is used for Date of Birth passwords?**


A: The format is **DDMmmYYYY** (e.g., 16Nov2002).


**Q: How is the identification number used as a password?**


A: The password will use the **last 6 characters** of the selected identification number, automatically converted to uppercase.


**Q: Can I send payslips to multiple employees at once?**


A: Yes, you can select all employees or multiple employees to send payslips in bulk.


**Q: Can I choose NRIC as the password option for Singapore payroll centers?**


A: Nope, to align with Singapore compliance requirements, the NRIC option will no longer be available as a payslip email password protection method. The Date of Birth will be the default and only password protection setting for Singapore payslip emails.








**Ownership**


By: Arveena


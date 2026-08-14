---
title: "How to Link Timetec Device in BrioHR Time and Attendance Module"
category: "Time and Attendance Integration"
subcategory: "Devices"
source_url: "https://support.briohr.com/knowledge/link-timetec-device-in-briohr-time-attendance"
date: "August 13, 2026"
---

# How to Link Timetec Device in BrioHR Time and Attendance Module

*Learn how to set up and integrate your Timetec TC10 device with BrioHR’s Time and Attendance module. Follow this step-by-step guide to enable integration, link device serial numbers, and synchronize employee information.*

### Introduction


BrioHR supports the integration of **Time and Attendance** with the third-party device, **Timetec Model TC10.**


Once the device integration feature has been enabled by the BrioHR team in your company’s account, you can proceed to configure and link your device directly within the **Time Attendance Policy** in BrioHR.


**Learn More: **[BrioHR Timetec Device Integration - First Time User Guide](https://support.briohr.com/hubfs/Knowledge%20Base%20Files/BrioHR%20Timetec%20Device%20Integration%20First%20Time%20User%20Guide_v2.0.pdf?hsLang=en)


---


### Step-by-Step Guide: Access the Time Attendance Policy


#### Step 1 - Log In to BrioHR Account


Log in to BrioHR account with your registered credentials.


#### Step 2 - Access the Time Attendance Policy


1. Go to **HR Lounge** > **Time Attendance.**


2. Navigate to **Policy.**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-05-2025-10-04-36-6747-AM.png?width=670&height=304&name=image-png-Nov-05-2025-10-04-36-6747-AM.png)
**


3. Open **any policy** that you would like to set up the device integration.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-05-2025-10-05-13-5678-AM.png?width=670&height=309&name=image-png-Nov-05-2025-10-05-13-5678-AM.png)


---


### Step-by-Step Guide: Set Up Device Integration


#### Step 1 - Enable Integration in Time Attendance Policy


1. On the policy page, go to **Other Configuration.**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-05-2025-10-05-43-2851-AM.png?width=670&height=214&name=image-png-Nov-05-2025-10-05-43-2851-AM.png)
**


2. Scroll down to **Integration.**


3. Toggle **ON** the **'Use Integration' **to enable it.


4. Click **Save.**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-06-2025-03-29-11-7698-AM.png?width=670&height=278&name=image-png-Nov-06-2025-03-29-11-7698-AM.png)
**


5. A confirmation message will appear - click** Proceed **to confirm.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-06-2025-03-28-44-2644-AM.png?width=670&height=225&name=image-png-Nov-06-2025-03-28-44-2644-AM.png)


**CAUTION:**


- When device integration is enabled,** the Facial Recognition** and **Geolocation** features in the policy will be automatically **disabled.**


**NOTE**:


For Device Integration using the TimeTec TC10 device, there are two available configuration options that organizations may choose from based on their operational preferences:


**Solution 1: Default Mode**
Employees are required to select an action type on the device before performing their attendance transaction.


**How it works:**
Employees must first select either **Clock In** or **Clock Out** on the device interface before verifying their attendance using fingerprint or facial recognition.


**Example:**
An employee selects **Clock In** then provides their fingerprint or facial recognition scan before starting work and selects **Clock Out** then provides the same verification at the end of the workday.





**Solution 2: First_Last Mode**
Employees can perform attendance verifications directly without selecting an action type on the device.


**How it works:**
Employees simply verify their attendance using fingerprint or facial recognition, and the system will automatically determine and record the first transaction as **Clock In** and the last transaction as **Clock Out**.


**Example:**
An employee taps the device upon arrival and again before leaving, while the system automatically captures the corresponding Clock In and Clock Out records.


**Optional Add-on for Solution 2: Track Break Time**


For clients on **Solution 2 (First & Last Log)**, BrioHR can additionally enable break-time tracking. When active, the system also identifies each employee's break-out and break-in punches within their configured break period — no extra action needed from employees at the device.


**Requirements and limitations:**


- - Only available for employees on **Shift mode** with a **break period configured** in their schedule. Employees on Flexi mode, or Shift mode without a break period, will continue to have only first-in/last-out captured.
  - Requires **Hybrid Attendance to be switched off** for the company. This is a temporary restriction — while break tracking is enabled, Hybrid Attendance cannot also be turned on for that company.
  - If an employee has an **odd number of punches** within their break window on a given day, the extra punch is flagged **"Incomplete"** rather than guessed — this will need HR Admin review on the timesheet.


**How to enable it:** Let your brioHR team know you'd like break tracking in addition to your Solution 2 setup when confirming your integration preference (see next section).


**Caution**: if **break tracking is enabled**, **Hybrid Attendance is disabled/blocked** for the company.


**Please ensure that the preferred solution is shared with our BrioHR team when the Integration is performed. **


####


#### Step 2 - Link the Device Serial Number in the Device Integration Log


1. Navigate to **Device Integration Log.**


2. Click** Link Device.**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-06-2025-03-43-09-0532-AM.png?width=670&height=161&name=image-png-Nov-06-2025-03-43-09-0532-AM.png)
**


3. Fill in the required details:


- **Name: **Assign a name for your device.
- **Device: **Timetec (default)
- **Serial Number: ** Enter the device serial number(found at the back of the device, or on the box)
- Description (Optional): Add details such as the device's location.


4. Click **Link Device** to save.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-06-2025-03-44-29-6116-AM.png?width=670&height=376&name=image-png-Nov-06-2025-03-44-29-6116-AM.png)


If the serial number is valid and already registered in the **Timetec Cloud**, the device will be successfully linked in the Device Integration Log.


**NOTE:**


If you have **subsidiary companies** that use the same devices, all devices set up/added for the main company will also be available for subsidiary companies.


However, please ensure that the employee ID remains unique for the main and the subsidiary. Two different employees cannot share the same ID (E.g., if both the main and subsidiary use a sequential running number as the employee ID).


**NOTE:**

If you have multiple Timetec devices, you must link each one individually.


---


### Step-by-Step Guide: Synchronize Employee Information


Once your Timetec device is linked, BrioHR will automatically **synchronize employee information** with the connected devices.


The following employee details will be synchronized automatically:


- **Employee ID Number**
- **Employee First Name**
- **Employee Last Name**


**NOTE:**

The system will synchronize both active and resigned employees. However, resigned employees will not appear in the BrioHR Time and Attendance timesheet.


For detailed instructions on enrolling and recording employees' biometric validation (fingerprint or facial recognition), please refer to our comprehensive guide:

[BrioHR Timetec Device Integration - First Time User Guide](https://support.briohr.com/hubfs/Knowledge%20Base%20Files/BrioHR%20Timetec%20Device%20Integration%20First%20Time%20User%20Guide_v2.0.pdf?hsLang=en)


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Nov-06-2025-04-04-17-1834-AM.png?width=670&height=292&name=image-png-Nov-06-2025-04-04-17-1834-AM.png)


---


### Frequently Asked Questions (FAQs)


**1. Which Timetec device models are supported by BrioHR?**


Currently, BrioHR supports the **Timetec TC10** model for device integration.


**2. Can I enable both device integration and facial recognition (BrioHR mobile app) at the same time?**


No. Once device integration is enabled, facial recognition and geolocation options (for mobile app time attendance) will be disabled as they are not compatible.


**3. What should I do if my device serial number cannot be linked?**


Ensure that the serial number of the TC10 Model is correctly entered. If the issue persists, contact **BrioHR Support**.


**6. Can I link multiple devices to the same BrioHR account?**


Yes, you can link multiple TC10 devices. Each device must be added individually in the **Device Integration Log**.


**7. Can I track employees' break time with Timetec device integration?**


Yes, for clients on Solution 2 (First & Last Log), and only if employees are on shift schedules with a break period defined in their shifts.


**8. Can I use Hybrid Attendance together with break tracking?**


Not currently.





**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


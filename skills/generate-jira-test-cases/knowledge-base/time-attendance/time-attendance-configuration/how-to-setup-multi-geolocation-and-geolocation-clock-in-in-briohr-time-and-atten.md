---
title: "How to Setup Multi-Geolocation and Geolocation Clock-in in BrioHR Time & Attendance"
category: "Time Attendance"
subcategory: "Time Attendance Configuration"
source_url: "https://support.briohr.com/knowledge/multi-geolocation-for-briohr-time-attendance"
date: "March 2, 2026"
---

# How to Setup Multi-Geolocation and Geolocation Clock-in in BrioHR Time & Attendance

*Learn how to configure Multi-Geolocation and Geolocation Clock-In in BrioHR Time Attendance to track employee clock-ins across multiple locations.*

### Introducing a new feature in the Time and Attendance module


The **Multi-Geolocation** feature in BrioHR’s Time & Attendance module allows employees to clock in and out from multiple approved locations. This is ideal for employees who work across different sites or offices during the week, for instance, clock in at Office A and clock out at Office B.


### When to Use Multi-Geolocation


- Employees regularly move between offices or job sites.
- You want to prevent clock-ins from unauthorized locations.
- You need accurate location-based attendance tracking.


### Mobile App Requirements


- Employees must use the **BrioHR mobile app** to clock in/out.
- They must grant the app permission to access their location.
- For location access setup, refer to **[[How to Enable Location Access](https://support.briohr.com/knowledge/enable-location-detection-for-accurate-clock-ins-briohr-mobile-app?hsLang=en)]**.


---


### Setting Up Multiple Geolocation


#### Step 1: Create Locations


Before assigning locations, create them in your BrioHR account Settings. For instructions, see** [[this guide](https://support.briohr.com/knowledge/how-to-create-tag-location-activity-and-workstation-for-work-shift?hsLang=en)].**


---


#### Step 2 : Assign Multiple Locations to a Shift (Shift Location)


1. In your BrioHR account, go to **Settings > Schedules & Shifts > Work Shifts.**


2. Edit the shift you want to update.


###


3. In the** Location** field, select multiple locations.


4. Click **Save.**


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-08-2025-07-43-19-3838-AM.png?width=670&height=353&name=image-png-Aug-08-2025-07-43-19-3838-AM.png)
**


**NOTE:**
**These shift locations will only apply if you enable Restrict Clock-in Location > By Shift Location in the Time Attendance Policy.**


---


#### Step 3: Configure Geolocation & Geofencing in the Time Attendance Policy


1. Navigate to **HR Lounge > Time Attendance > Policy**.


2. Edit a policy and open **Other Configuration**.


3. Toggle On the **'Clock In/Out with Location Tracking'.**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-08-2025-07-37-45-6250-AM.png?width=670&height=269&name=image-png-Aug-08-2025-07-37-45-6250-AM.png)


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-08-2025-07-37-51-1010-AM.png?width=670&height=312&name=image-png-Aug-08-2025-07-37-51-1010-AM.png)
**
---


#### Step 4: Choose a Location Restriction Option


**NOTE: **
**This triggers geofencing and employees must clock in/out at the designated locations.**


**Option A - Shift Location**


- Employees can only clock in at locations assigned to their shift.
- If no shift location is assigned, the system will default to any configured custom location.
- If no custom location is set, there will be no location restriction.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-11-2025-04-04-34-8751-AM.png?width=670&height=158&name=image-png-Aug-11-2025-04-04-34-8751-AM.png)


**Option B - Custom location**


- Employees can clock in at any pre-configured custom location set in the policy.
- You can add more than one custom location.


- To create/add a new location, click on **+Add Location** button


**NOTE:**


**If both Shift Location and Custom Location are enabled, Shift Location will take priority.**


**IMPORTANT:**

**Do not forget to click on 'Save' to save your changes!**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-11-2025-04-07-20-7041-AM.png?width=670&height=254&name=image-png-Aug-11-2025-04-07-20-7041-AM.png)


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-11-2025-03-16-46-1614-AM.png?width=670&height=320&name=image-png-Aug-11-2025-03-16-46-1614-AM.png)
**


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Aug-11-2025-04-09-52-2816-AM.png?width=670&height=287&name=image-png-Aug-11-2025-04-09-52-2816-AM.png)


---


#### Frequently Asked Questions (FAQ)


**
Q1: Can I set different geolocations for different shifts?**


A: Yes. Assign the relevant locations when editing the work shift.


**Q2: What happens if no location is set in the shift?**


A: The system will not restrict clock-in location unless custom locations are configured in the policy.


**Q3: Can employees clock in/out from their web browser login?**


A: No. Once location restriction is enabled in the Time Attendance policy, the employees must clock in/out from their mobile phone > BrioHR App.


The app will track their location during the clock in/out action.


**Q4: Can employees clock in/out outside of the assigned locations?**


A: No. The system will prevent the employees from continuing their clock in/out actions if their current locations are outside of the assigned locations.





**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*


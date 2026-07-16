---
title: "Import Employee Time Attendance Data (SFTP Integration) for Clock-In and Clock-Out"
category: "Time and Attendance Integration"
subcategory: "SFTP"
source_url: "https://support.briohr.com/knowledge/import-employee-time-attendance-data-sftp-integration-for-clock-in-clock-out"
date: "March 6, 2026"
---

# Import Employee Time Attendance Data (SFTP Integration) for Clock-In and Clock-Out

*This article is a guide on how to create a timelog SFTP integration to import employee clock-in and clock-out data into BrioHR for accurate timesheet records in the Time Attendance module.*

**IMPORTANT:**


**To enable this integration, you will need to contact our support team via email or live chat so we can provide the necessary access. Please contact us via: **


- **Email: *[support@briohr.com](mailto:support@briohr.com)***
- **Live chat: Available 9 am - 6 pm (Kuala Lumpur working days)**


**Note: ****If you are still in the implementation stage, please reach out to your implementation manager for support.**


The integration flow with BrioHR will consist of the steps below:


1. BrioHR will create the credentials for client. Consists of: User credentials and password
2. Client can try to connect to upload the data using FileZilla or Terminal (SFTP Command).


#### Host and Port Details


| Host | time-attendance-sftp.briohr.com |
| --- | --- |
| Port | 2222 |
| User | will be provided by BrioHR |
| Password | will be provided by BrioHR |


####


#### File Format


#### Fields:


#### Specifications:


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Mar-04-2026-04-46-39-5063-AM.png?width=562&height=256&name=image-png-Mar-04-2026-04-46-39-5063-AM.png)


####


#### Example


1. Delimiter-Separated Values (Without Header)


**Comma-separated values**


```
"EMP 001", "2025-07-11T02:10:21Z", "clock_in""EMP 001", "2025-07-11T11:01:43Z", "clock_out"
```


**Space-separated values
**


```
"EMP 001" "2025-07-11T02:10:21Z" "clock_in""EMP 001" "2025-07-11T11:01:43Z" "clock_out"
```


**Pipe-separated values**


```
"EMP 001" | "2025-07-11T02:10:21Z" | "clock_in""EMP 001" | "2025-07-11T11:01:43Z" | "clock_out"
```


**Important:**


When no header is present, the values must strictly follow the order: `employeeInternalId`, `timestamp`, `action`.





2. Delimiter-Separated Values (With Header)


If a header is present, the order of the values can be different from the required field order, as long as the header accurately defines the fields.


**Example (Valid with Header)**: In this example, the order is `internalId`, `action`, `timestamp`, which is valid because the header is present.


```
"internalId", "action", "timestamp""EMP 001", "clock_in", "2025-07-11T02:10:21Z""EMP 001", "clock_out", "2025-07-11T11:01:43Z"
```


**Example (Invalid without Header)**: This is **invalid** because there is no header, and the order of the values (`employeeInternalId`, `action`, `timestamp`) is incorrect.


"EMP 001", "clock_in", "2025-07-11T02:10:21Z""EMP 001", "clock_out", "2025-07-11T11:01:43Z"




3. JSONL Format


JSONL (JSON Lines) means each line in the file is a valid JSON object.


```
{"employeeInternalId":"EMP 001", "timestamp":"2025-07- 11T02:10:212", "action": "clock_in"}{"employee InternalId":"EMP 001", "timestamp":"2025-07- 11T11:01:43Z", "action": "clock_out"}
```


####


**Important:**


- Timestamp must be in ISO 8601 UTC format (with 'Z' suffix).
- Action field accepts only "clock_in" or "clock_out" values.


####


#### Upload


You can upload your file using either **FileZilla** or a **Terminal** SFTP command.


#### FileZilla


1. Download [FileZilla](https://filezilla-project.org/download.php?type=client).
2. Enter your credentials and click **Quickconnect**.
3. Right-click the file you wish to upload and select **Upload**.


**Note on Server Limitation:** Due to a limitation of the SFTP server, the server may still appear empty even after a successful file upload.




#### Terminal (SFTP Command)


1. Login using your credentials:


```
sftp -P 2222 <your_user>@time-attendance-sftp.briohr.com
```
2. Enter your password when prompted:


```
<your_user>@time-attendance-sftp.briohr.com's password:
```
3. Once connected, use the `put` command to upload your file:


```
sftp> put <file_path>
```


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Mar-04-2026-05-50-30-0129-AM.png?width=670&height=155&name=image-png-Mar-04-2026-05-50-30-0129-AM.png)





***Need Assistance?***


*If you have any questions regarding the API above or require assistance, please reach out to our support team via live chat or email us at support@briohr.com.*


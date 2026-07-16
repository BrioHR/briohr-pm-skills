---
title: "BRIOHR API INTEGRATION FLOW"
category: "API Integrations"
subcategory: "API"
source_url: "https://support.briohr.com/knowledge/briohr-api"
date: "June 5, 2026"
---

# BRIOHR API INTEGRATION FLOW

*BrioHR provides the APIs integration for clients to enable seamless data exchange and automation between both platforms. This integration will enhance operational efficiency, reduce manual data entry, and improve overall user experience.*

### Project Overview


BrioHR provides the APIs integration for clients to enable seamless data exchange and automation between both platforms. This integration will enhance operational efficiency, reduce manual data entry, and improve overall user experience. BrioHR will provide comprehensive integration documentation to ensure smooth implementation and compatibility with the partner's system.


We provide the APIs that can be used by client to pull the data from our system into client’s system for any purpose that needed by client.


**1. Integration Flow**





![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-07-2025-01-45-50-0827-AM.png?width=670&height=444&name=image-png-Jul-07-2025-01-45-50-0827-AM.png)


The integration flow with BrioHR will consists of:


1. Client request for the APIs/integration access together with the list of IPs (recommended for securing the line of integration).
2. BrioHR will create the credentials for client. Consists of: Authentication credentials and client’s ID.
3. Client can try to connect to BrioHR API using the link, authentication & ID.





### 2. Specifications


***Transport Mechanism ***


**Protocol: **HTTP/HTTPS


**Base URL:**** **https://static.api.briohr.com


**Request Format: **JSON/CSV


**Response Format: **JSON or CSV (specified via Accept header)


**Character Encoding: **UTF-8


***Authentication ***


**Method: ***API Key *in Headers


**Header Name:**** **Authorization


**Example: **


1 curl --location 'https://static.api.briohr.com/v2/api/external/reports/employees-main-information/download? format=csv' \


2 --header 'Authorization: Basic aHotYXBwOmJyaW9ocg=='


***Response Sample ***


*json *


1 {


2 "id": 1,


3 "name": "record 1"


4 }


*csv *


1 id,name


2 1,record 1





### 3. Features


**3.1 [Employee Data Synchronization](https://support.briohr.com/knowledge/employee-details-api-integration?hsLang=en)**


Automatic synchronization of employee records between BrioHR and the partner system. Real-time employee data tracking with the partner’s platform.


Support for viewing list of employee profiles.





**3.2 [Leave Synchronization](https://support.briohr.com/knowledge/leave-summaries-api-integration?hsLang=en)**


Integration of leave summary records.


Real-time leaves records tracking with the partner’s platform.





**3.3 [Claim Management](https://support.briohr.com/knowledge/claim-report-api-integration?hsLang=en)**


Integration of claim reports.


Real-time claim records tracking with partner’s platform.


Updating reimbursement status from client to BrioHR.





**NOTE: **


 If you would like to **exclude payroll information** from the API integration, this option can be **enabled upon request (except for the Company Payroll Report).**


Please contact our support team to let us know, and we will assist with configuring the setting for your account.


### 4. Integration Documentation


BrioHR will provide detailed documentation, including:


API endpoints and request/response structures.


Authentication and security guidelines.





### 5. Use Cases


#### 5.1 How to pay claims from an accounting system


Client that has an accounting system can be integrated with BrioHR.


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-07-2025-02-03-20-3692-AM.png?width=670&height=461&name=image-png-Jul-07-2025-02-03-20-3692-AM.png)


Scenario:


1. Client has their own existing accounting system, manage and process all claim reports
2. Client will use BrioHR’s claim & payroll modules for recording and reimbursing the claims. Explanation of flow:
3. Once employee create the claim report, data can be pulled into client’s accounting system. 2. After the claim report processed, client can call BrioHR’s claim API to change & process the reimbursement. 3. Both system will have an up-to-date data to be sync each other.


*Sample of data mapping for downloading claim’s reports *


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-07-2025-02-13-06-2646-AM.png?width=470&height=260&name=image-png-Jul-07-2025-02-13-06-2646-AM.png)


*Sample of data mapping for update claim’s status (accept csv format only) *


![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-07-2025-02-15-47-7151-AM.png?width=538&height=224&name=image-png-Jul-07-2025-02-15-47-7151-AM.png)





#### 5.2 How to sync the employee list with reporting system


**
![image](https://support.briohr.com/hs-fs/hubfs/image-png-Jul-07-2025-02-07-48-5049-AM.png?width=670&height=230&name=image-png-Jul-07-2025-02-07-48-5049-AM.png)
**


Scenario:


1. Client has their reporting dashboard.
2. Client wants to show the employee’s data for their analytics.


Explanation of flow:


1. Client can setup the scheduler to call BrioHR’s API for grabbing all employee data and details.
2. Client can use that data and show them as an analytics report in their internal dashboard


**
**


**Ownership**


By : Arveena


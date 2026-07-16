---
title: "BrioHR Data Backup and Recovery Policy: Ensuring HR Data Security"
category: "FAQs"
subcategory: "Account"
source_url: "https://support.briohr.com/knowledge/briohr-data-backup-and-recovery-policy-ensuring-hr-data-security"
date: "August 22, 2025"
---

# BrioHR Data Backup and Recovery Policy: Ensuring HR Data Security

*BrioHR protects HR data with secure backup and recovery measures. Learn how BrioHR ensures compliance, resilience, and peace of mind.*

BrioHR is a secure **cloud-based HR software** that runs on **Amazon Web Services (AWS)**. As a **multi-tenant SaaS application**, data protection, backup, and recovery are critical to ensuring uninterrupted HR operations and compliance. This article outlines how **BrioHR safeguards employee data** through daily backups, secure storage, and reliable recovery protocols.


### Data Backup Policy


#### How often is data backed up?


BrioHR performs **daily backups, four times per day, **of all data in **MongoDB format** to ensure **comprehensive data protection**. BrioHR also employs a two-tiered backup strategy to ensure maximum data protection and recovery flexibility:


- **Continuous Cloud Backups**: We perform continuous backups with WAL **archiving** every minute. This enables **Point-in-Time Recovery (PITR)**, allowing for granular data restoration to any specific moment in time.
- **Scheduled Snapshots**: We take full database snapshots on a defined schedule for comprehensive data restoration. This includes:

  - **Daily backups**, retained for 30 days.
  - **Weekly backups**, retained for 52 weeks.


#### What database does BrioHR use?


BrioHR operates on **MongoDB**, a flexible and scalable database designed to handle high-volume HR data efficiently.


#### How many sets of backups does BrioHR have?


BrioHR maintains **one set of backup stored across multiple AWS Availability Zones (AZs)** to ensure redundancy and resilience.


---


### Cloud Hosting and Security


#### Which cloud service provider does BrioHR use?


BrioHR is hosted on **Amazon Web Services (AWS)**, a global leader in cloud security and compliance.


#### Where are BrioHR’s off-site locations?


All data is **physically stored in Singapore**, within AWS data centers. Data is synchronized across **three separate availability zones**, meaning that if one data center experiences downtime, another automatically takes over without disrupting service.


---


### Data Recovery Policy


#### How does data restoration occur?


BrioHR complies with strict **Service Level Agreements (SLA)**, including:


- **Recovery Point Objective (RPO):** 30 minutes
- **Recovery Time Objective (RTO):** 1 day


#### How often is data restored?


Data restoration is performed **only when necessary**, such as in the event of a system failure or incident.


#### Does BrioHR perform restoration tests?


Yes, BrioHR conducts **restoration tests** every 6 months.


---


### Key Takeaways


- **Daily backups** in MongoDB format
- **Hosted on AWS Singapore data centers**
- **Redundant backups across three availability zones**
- **RPO: 30 minutes | RTO: 1 day**
- **Restoration tests possible** upon request





BrioHR ensures that all **employee data remains protected, compliant, and quickly recoverable**—giving businesses peace of mind while managing their workforce in the cloud.


For full details on how we protect your data, visit our [Privacy Policy](https://briohr.com/privacy-policy/) and [Trust Center](https://trust.briohr.com/).





**Need Assistance?**


*If you have any questions or require assistance, please reach out to our support team via live chat or email us at [support@briohr.com](mailto:support@briohr.com).*








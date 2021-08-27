# CP4S 300 Use Case Demonstration Data Exfiltration

## 1 Use Case overview

Objective: Detect and contain data leakage quickly

Challenge: Find out the real cause and, if appropriate, trace it back to internal misuse

Stakeholder: SOC analysts, CISO, Data Security Specialist 

Outcome: Incident of data misuse clarified in detail. Actual cause uncovered, attackers involved identified, required response actions initiated to contain incident and protect data from further leakage.

## 2 Assumptions, Requirements & Setup

-	Cloud Pak for Security (CP4S) version 1.6x on IBM ROKS instance is up and running
-	QRadar Dashboard Populator System Connected in proxy mode, along with AppHost with Ansible app installed 
-	Setup the required data sources with names of your choice using the STIX bundles:
     - qradar102.json 
     - guardium102.json 
     - carbonblack102.json 
- Add CAR (Connect Asset and Risk) data. CAR data is added through API using the provided json file 
  - CARData_UC_DataExFil.json 
  
Please see details in file: "CP4S 300 Demo Guide - Data Exfiltration.pdf"

## 3 Demo Use Case detailed Outline

### UC Context:
- Data breach is detected by data security solution e.g. Guardium Data Protection
- Policy alert is triggered (in Guardium) and automatically forwarded to QRadar
- QRadar offense is automatically created based on the forwarded alert
- In parallel, a QRadar event is triggered based on an outbound data flow containing a suspicious content alert / SuspectContent_SensitiveData_Detected
- QRadar offense is enriched with event & flow data “Outbound transfer of sensitive data(PII)” 
- Case is automatically created in CP4S SOAR from QRadar offense
- Dynamic SOAR playbook is triggered and appropriate data breach tasks are automatically added as PII data is affected
- Get insights into data violation alert:
  - SOC analyst checks newly created cases with high severity from CP4S dashboard
- Investigate alert / initiate security case:
	- Analyst verifies the case in CP4S SOAR and makes changes as appropriate
	- SOAR playbook tasks are dynamically updated after the incident type in case is changed to phishing
- Analyze who, what, from where; Enrich case:
	- Data investigation is performed by analysts using CP4S Data Explorer to identify actual root cause, user and attackers involved
	- The analyst enriches the case with the insights/artifacts gained from the analyses with CP4S Data Explorer 
- Gather context information:
	- Threat data can be additionally collected to enrich the case using the X-Force threat data in CP4S TII or data from third-party feeds
- Verify asset criticality:
	- Using the information in the CP4S CAR database, the analyst verifies the asset context and criticality 
- Triage security case / response activities:
  - Automatic or manual task are triggered through SOAR to:
	  - notify owners of systems used for phishing attack
	  - report suspicious activity to the FTC
	  - create a ticket in Service Now (SNOW)
       - block access to database for suspicious internal user
	  - update the firewall to block IP 
       - using an Ansible workflow  
  

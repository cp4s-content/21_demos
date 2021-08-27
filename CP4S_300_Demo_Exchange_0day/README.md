# Cloud Pak for Security Demo

## Microsoft Exchange 0-Day

*Created By: Jonathan Tomasulo*

## Demo Resources

- [Microsoft Exchange Article](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)
- STIX File 1: https://cloud-pak-demo-files.mybluemix.net/21_demos/CP4S_300_Demo_Exchange_0day/processes.stix.json
- STIX File 2: https://cloud-pak-demo-files.mybluemix.net/21_demos/CP4S_300_Demo_Exchange_0day/palo.stix.json
- STIX File 3: https://cloud-pak-demo-files.mybluemix.net/21_demos/CP4S_300_Demo_Exchange_0day/exchange.stix.json
- Resilient File: https://cloud-pak-demo-files.mybluemix.net/21_demos/CP4S_300_Demo_Exchange_0day/export-soar-hafnium.resz

## Demo

### Open

As I am sure most of you are well aware, the hacking group known as HAFNIUM, made the news on March 2nd 2021. HAFNIUM took advantage of a Microsoft Exchange 0-Day vulnerability that allows remote attackers to takeover on prem exchange servers, exfiltrate data from the target network as well as establish web shells on those servers for further use.

With this in mind I am going to walk you through how we can use a well tuned cloud pak for security environment to scan for known indicators of compromise, gain further context on what happened, and ultimatly remediate the threat.

### Threat Intelligence Insights

* We are going to get started by executing a search for the phrase "HAFNIUM"
* From there I can see that X-Force has a collection that is directly related to this particular attack.
* So if I click on that I can read through the overview, understand the TTPs, and download YARA rules to use for detection of this exploit.
* One tab over I have a list of the known IOCs related to the Exchange Vulnerability.
* Finally I can use this data to simply execute a 1 click federated search for all of these IOCs across my entire infrastructure. This scan should take about 30 seconds to a few minutes depending on the size and speed of your network. For the sake of time I ran mine just before this demonstration.
* You will notice that we found 8 different indicators of compromise.
* You will also notice that this automatically created a brand new case for us to use for incident response a bit later.
* Before I jump directly into the incident response process I want to understand a little more about these indicators and how they relate to my local resources so that I can do a proper remediation.
* So I will start off with this IP address. If I right click on it I can simply execute a new query from this screen.
* I will search all data sources for the last 48 hours.

### Data Explorer

* We can see here that this IP Address is the location that launched the attack against the Exchange Server. You can see as we go through they established the connection with SMTP::HELO and then started to pull back data with SMTP::DATA.
* From there I can pivot on the 192.168.1.10 address to understand more about what else this internal IP was doing.
* From the results I can see that this IP Address is reaching out to the mega.nz service which from reading this microsoft article is perfectly in line with what we are seeing from the microsoft threat write up.
* This traffic with mega.nz is perfectly inline with what we are expecting from this attack. If we look back at the original article from microsoft, they are saying that mega is the way in which the attackers are exfiltrating the data. So this is cause for further concern.
* At this point I can begin to add some of these items as artifacts to the case for safe keeping later on.
* If I go to my left hand side into the search data I can look at all my IP Addresses that I can see are reaching out to mega.nz
* And as I go forward I can continue to search on other hashes and gather more intelligence around other assets or users that may have been affected by this.
* For demonstrations sake I will stop here and move into incident response.

### Cases

* You will notice that automatically, there is a case created for us and we have already begun to enact some automated techniques to quickly remediate the issue.
* We also have a set of manual tasks to complete, some of which have been assigned to an incident responder and have a due date assigned to them. You will also notice that each task comes with a set of instructions for the incident responder. This helps bring newer incident responders up to speed and provide a place for more seasoned incident responders to codify their knowledge.
* We can enter into the details tab and further tweak the nuances of this particular incident which will in turn add or subtract tasks from our playbook.
* We can also come into the data compromise tab and specify which regulatory compliance mandates you are under to add new tasks and maintain compliance.
* Last I can look at all the artifacts that have been added to this case from TII and my own manual investigation.

### Close

- So in closing we have walked through an entire discovery, investigation, and incident response workflow.
- This was made possible by a highly integrated Security platform that is easily expandable and houses a number of critical security capabilities.
# CP4S 300 Ryuk Ransomware 

## 1 Demo Use Case overview

Ryuk ransomware has been infecting victims since around 2018 and it is believed to be based on the source code of Hermes ransomware, which was sold on an internet hacking forum back in 2017. Since its inception, Ryuk has been used to target large organizations to great effect, having accumulated as much as $61.26 million (as of Feb 2020) in ransom payments according to federal investigations. 

One of the reasons behind Ryuk’s unfortunate success is the threat actor’s capacity to evolve their tactics, techniques and procedures (TTPs). 

Ryuk ransomware is most often seen as the final payload in a larger targeted attack against a corporation, and since its return in September 2020, it has been mainly via TrickBot or BazarLoader infections.

The objective of this demo is to highlight how you can prevent the execution and manage the distribution of this aggressive Ransomware leveraging on the Threat Intelligence Insight, Data Explorer and SOAR capabilities of the Cloud Pak for Security.


## 2 Assumptions, Requirements & Setup

- Use of the IBM ROKS Demo Environment – CP4S 1.6 Version
- Review the attack details to be familiar with the Ryuk Ransomware:

https://labs.sentinelone.com/an-inside-look-at-how-ryuk-evolved-its-encryption-and-evasion-techniques/?utm_adgroup=116406398635&utm_type=b&utm_target=dsa-19959388920&utm_device=c&utm_medium=cpc&utm_source=google&utm_campaign=11908697661&utm_content=488145339253&utm_term=&gclid=Cj0KCQjwmIuDBhDXARIsAFITC_4EukIOfltdVC3J_85shZCvcjT8mJeJz4pY89D0Naku3LxVdOgRXSIaAuf0EALw_wcB

https://www.cybereason.com/blog/cybereason-vs.-ryuk-ransomware

---
id: 5G_Network_Architecture
aliases: []
tags:
  - electronics
  - communication
  - wireless
  - digital_communication
Date: 13-10-2024
dg-publish: true
---
# 5G Network Architecture

```mermaid
graph LR 
A[5GC] --> B[Baseband Unit] 
B --> C[Remote Radio Head] 
C --> D[UE]

```

**UE**-> User Equipment 
**Downlink Direction**: When the user receives(gNodeB --> User)
**Uplink Direction**: When the user transmitts (UE --> gNodeB)

**Base Station(gNodeB)**: Remote Radio Head + Baseband Unit

#### History
1. **1G**: Based on analog transmission (AM FM)
	- AMPS(Advanced Mobile Phone System) Developed within North America
	- NMT(Nordic Mobile Telephony) By Network operators of Nordic 
	- TACS(Total Access Communication System) , used by UK
>- Only Voice Service
2. **2G**: Introduced Digital Transmission 
	- **GSM**(Global System For Mobile Communication) By European Countries 
	- D-AMPS(Digital AMPS) ,North America 
	- PDC(Personal Digital Cellular) , Japan
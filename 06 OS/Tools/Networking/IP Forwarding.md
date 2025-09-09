---
id: IP_Forwarding
aliases: []
tags:
  - os
  - tools
  - networking
Date: 2024-08-04
cssclasses: 
dg-publish: true
---
# IP Forwarding
>[!info|right-small] To check current ip_forwarding  status
>```bash
>sysctl net.ipv4.ip_forward
>```

IP Forwarding is the process that allows a system to route the traffic between one network interface to an other. 
eg: Forward my `usb0`'s network to `eth0`
## Contents
- [[#Enable IP Forwarding]]

#### Enable IP Forwarding 

```bash
sudo sysctl -w net.ipv4.ip_forward=1

```

This will enable temporarly to make it premenent

```bash
# sudo nano /etc/sysctl.conf
net.ipv4.ip_forward=1

```

Now apply the changes

```bash
sudo sysctl -p

```

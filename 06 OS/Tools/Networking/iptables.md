---
id: iptables
aliases: []
tags:
  - os
  - tools
  - networking
Date: 2024-08-04
dg-publish: true
---
# iptables

## Contents
- [[#Setting up NAT to share trafic]]

#### Setting up NAT to share trafic

```bash
sudo iptables -t nat -A POSTROUTING -o usb0 -j MASQUERADE 
sudo iptables -A FORWARD -i eth0 -o usb0 -j ACCEPT 
sudo iptables -A FORWARD -i usb0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT

```

2. Persist the iptables Rules

```bash
sudo iptables-save > /etc/iptables/iptables.rules
sudo systemctl enable iptables
sudo systemctl start iptables

```
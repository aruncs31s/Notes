---
id: Virtmanager
aliases: []
tags:
  - os
  - tools
Date: "05-03-25"
dg-publish: true
---
# Virtmanager

- *virt manager default network not active* [Source](https://www.reddit.com/r/VFIO/comments/6iwth1/network_default_is_not_active_after_every/)

```bash
sudo virsh net-autostart default
sudo virsh net-start default

```
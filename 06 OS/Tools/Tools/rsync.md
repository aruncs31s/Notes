---
id: rsync
aliases: []
tags:
  - os
  - tools
dg-publish: true
---
# rsync

Created : 2024-05-28 20:59

## Contents

#### Basic Usage

```bash
rsync [options] source destination

```

#example

```bash
rsync -arch -v /home/user/Pictures/ /mnt/BACKUP/Pictures/

```

-> -a : preserve `permissions` , `timestamps` , `symbolic links`
-> -v : verbose
-> -h : human readable
-> -c : compress

> [!warning] Naming conventions
> Never Put ==/path/to/somethng== insted use ==/path/to/something/==

###### Unexpected behaviour

```bash
rsync 1 2

output :
├── 1
│   ├── 1
│   │   └── 2
│   ├── 2
│   │   └── 3
│   ├── 3
│   ├── 4
│   │   └── 5
│   └── 5
└── 2
    └── 1
        ├── 1
        │   └── 2
        ├── 2
        │   └── 3
        ├── 3
        ├── 4
        │   └── 5
        └── 5

```

###### Expected behaviour 2

```bash
rsync 1/ 2/

output:
├── 1
│   ├── 1
│   │   └── 2
│   ├── 2
│   │   └── 3
│   ├── 3
│   ├── 4
│   │   └── 5
│   └── 5
└── 2
    ├── 1
    │   └── 2
    ├── 2
    │   └── 3
    ├── 3
    ├── 4
    │   └── 5
    └── 5

```

#### Copying over ssh

1. From ssh to local

```bash
rsync [options] user@ip:/path/ destination --rsync-path=/bin/rsync

```

2. From Local to ssh

```bash
rsync [options] source user@ip:/path/ --rsync-path=/bin/rsync

```

4. Arch -> PI

| Command      | Doings             |
| ------------ | ------------------ |
| `--progress` | Shows the progress |
| `z`          | compress           |

#### With Crontab

```bash
crontab -e

```

```bash
0 2 * * * rsync -avh --delete /path/to/source/ /path/to/destination/

```

## References

1. [Crontab](https://www.tutorialspoint.com/unix_commands/crontab.htm)

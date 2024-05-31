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
-> -h : human redable  
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

## References
1. 
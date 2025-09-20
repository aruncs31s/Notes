---
id: MySQL
aliases: []
tags:
  - coding
  - database
dg-publish: true
---
# MYSQL 
- [[MariaDB]]

```

 jODe+,cTA1u#

```

```

2025-08-01T05:34:21.328015Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
2025-08-01T05:34:21.328578Z 0 [Warning] [MY-010915] [Server] 'NO_ZERO_DATE', 'NO_ZERO_IN_DATE' and 'ERROR_FOR_DIVISION_BY_ZERO' sql modes should be used with strict mode. They will be merged with strict mode in a future release.
2025-08-01T05:34:21.328603Z 0 [System] [MY-013169] [Server] /usr/bin/mysqld (mysqld 9.3.0) initializing of server in progress as process 40719
2025-08-01T05:34:21.340959Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2025-08-01T05:34:21.730087Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2025-08-01T05:34:22.749290Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: jODe+,cTA1u#
2025-08-01T05:34:24.661607Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.

~
❯

```

before deleting /var/lib/mysql

```

2025-08-01T05:33:26.705728Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
2025-08-01T05:33:26.706637Z 0 [Warning] [MY-010915] [Server] 'NO_ZERO_DATE', 'NO_ZERO_IN_DATE' and 'ERROR_FOR_DIVISION_BY_ZERO' sql modes should be used with strict mode. They will be merged with strict mode in a future release.
2025-08-01T05:33:26.706678Z 0 [System] [MY-013169] [Server] /usr/bin/mysqld (mysqld 9.3.0) initializing of server in progress as process 38377
2025-08-01T05:33:26.708198Z 0 [ERROR] [MY-010457] [Server] --initialize specified but the data directory has files in it. Aborting.
2025-08-01T05:33:26.708202Z 0 [ERROR] [MY-013236] [Server] The designated data directory /var/lib/mysql/ is unusable. You can remove all files that the server added to it.
2025-08-01T05:33:26.708244Z 0 [ERROR] [MY-010119] [Server] Aborting
2025-08-01T05:33:26.708570Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.

```

## Install 

```bash
sudo pacman -S mysql

```

```bash
sudo mysqld --initialize --user=mysql --basedir=/usr --datadir=/var/lib/mysql

```

```txt
 A temporary password is generated for root@localhost: p>uLzaSsl9p!

```

## Setup 
@initial

```bash
sudo mysqld_safe --skip-grant-tables --skip-networking &
mysql -u root

```

```mysql
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_password';
FLUSH PRIVILEGES;
EXIT;

```
---
id: MariaDB
aliases: []
tags:
  - coding
  - database
dg-publish: true
---
# MariaDB
Created : 2024-06-02 15:53
## New Install 

```bash
sudo pacman -S mariadb 
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

```

```

Installing MariaDB/MySQL system tables in '/var/lib/mysql' ...
OK

To start mariadbd at boot time you have to copy
support-files/mariadb.service to the right place for your system

Two all-privilege accounts were created.
One is root@localhost, it has no password, but you need to
be system 'root' user to connect. Use, for example, sudo mysql
The second is mysql@localhost, it has no password either, but
you need to be the system 'mysql' user to connect.
After connecting you can set the password, if you would need to be
able to connect as any of these users with a password and without sudo

See the MariaDB Knowledgebase at https://mariadb.com/kb

You can start the MariaDB daemon with:
cd '/usr' ; /usr/bin/mariadbd-safe --datadir='/var/lib/mysql'

You can test the MariaDB daemon with mariadb-test-run.pl
cd '/usr/mariadb-test' ; perl mariadb-test-run.pl

Please report any problems at https://mariadb.org/jira

The latest information about MariaDB is available at https://mariadb.org/.

Consider joining MariaDB's strong and vibrant community:
https://mariadb.org/get-involved/

```

## QuickStart 

```mysql
CREATE DATABASE myapp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

```

```sql
CREATE USER 'gouser'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON myapp_db.* TO 'gouser'@'localhost';
FLUSH PRIVILEGES;
-- Verify 
SHOW DATABASES;
SELECT user, host FROM mysql.user WHERE user = 'gouser'; 
EXIT;

```

## Contents
- 
  
### Basics
1. [[Tables]]
#### Entering into the CLI

```bash
mysql -u root -p

```

used to access the MySQL command-line interface (CLI) as the root user, which has the highest level of privilage. `-p` asks for password

```bash
mysql -p 

```

This will drop into the local user ;

#### Creating A New User

```sql
CREATE USER '<newuser>'@'%' IDENTIFIED BY 'password';

```

- replace the `newuser` with desired name , i used my USER_NAME 
- replace the password 

#### Simple Example
[Reference](https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/)

##### Countries example
[Reference](https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/)

![](https://www.mariadbtutorial.com/wp-content/uploads/2019/10/mariadb-sample-database.png)

##### Hostel Room and Members
1. Need to create __somthing that stores the room id = room number__
2. Insert the members as elements of the table.

1. 

```sql
CREATE TABLE rooms ( room_number INT PRIMARY KEY, member VARCHAR(100) );

```

2. 

```sql
INSERT INTO rooms (room_number, member) VALUES (1, 'Someone_1'), (2, 'Someone_2');

```

## References
1. https://www.mariadbtutorial.coR
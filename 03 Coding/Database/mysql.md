---
id: mysql
aliases: []
tags:
  - coding
  - database
dg-publish: true
---
# mysql
Created : 2024-06-02 04:11

## Contents
- 

### First Time setup
#### Arch

```bash
mysqld_safe --user=mysql &

```

### Basics
- `SELECT` - extracts data from a database
- `UPDATE` - updates data in a database
- `DELETE` - deletes data from a database
- `INSERT INTO` - inserts new data into a database
- `CREATE DATABASE` - creates a new database
- `ALTER DATABASE` - modifies a database
- `CREATE TABLE` - creates a new table
- `ALTER TABLE` - modifies a table
- `DROP TABLE` - deletes a table
- `CREATE INDEX` - creates an index (search key)
- `DROP INDEX` - deletes an index

#### MySQL vs MariaDB
1. MySQL
MySQL is an open-source relational database management system(RDBMS) based on Structured Query Language (SQL)
1. MariaDB 
MariaDB is an open source relational database management system (RDBMS) that is a compatible drop-in replacement for the widely used MySQL database technology.

##### Create DATABASE

```sql
CREATE DATABASE [IF NOT EXISTS] database_name

```

1. Selecting a database

```sql
USE <database_name>

```

*It does not require a ;*

## References
1. https://www.mariadbtutorial.com
2. https://www.w3schools.com/mysql/
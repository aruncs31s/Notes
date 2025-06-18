# MariaDB
Created : 2024-06-02 15:53


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
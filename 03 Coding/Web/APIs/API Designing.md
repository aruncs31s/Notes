# API Designing 

```
2025/08/01 17:33:36 /home/aruncs/Work/etlab-backend-go/modules/staff/handler/register_staff_details.go:67 sql: Scan error on column index 2, name "dob": unsupported Scan, storing driver.Value type []uint8 into type *time.Time
[0.389ms] [rows:1] SELECT * FROM `s
```

This error occurs because the MySQL driver is returning the date as a byte slice (`[]uint8`) instead of a `time.Time` that GORM expects. This is a common issue with MySQL date/datetime handling in Go.

Here are several solutions:

## Solution 1: Add `parseTime=true` to your database connection string

This is the most common fix. Update your database connection string to include `parseTime=true`:
```go
// Example connection string
dsn := "username:password@tcp(localhost:3306)/database_name?charset=utf8mb4&parseTime=true&loc=Local"
db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
```


# Eager Loading 
>Prevents
- [[N+1 Problem]]

**Eager loading** solves this by fetching related data _in advance_, usually with a SQL `JOIN` or an additional precomputed query.

```go
var users []User
db.Preload("Orders").Find(&users)
```

```sql
SELECT * FROM users
SELECT * FROM orders WHERE user_id IN (...)    
```

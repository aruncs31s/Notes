# N+1 Problem 

Imagine you have two database tables:
- `users`
- `orders` (each order belongs to a user)
Now you want to list all users and the orders they made.
If you write this naively:

```go
var users []User
db.Find(&users)
for _, u := range users {
    db.Where("user_id = ?", u.ID).Find(&u.Orders)
}

```

This does:
- 1 query to get all users → `SELECT * FROM users`
- **N queries** (one per user) to get their orders → `SELECT * FROM orders WHERE user_id = ?`
So if you have 100 users, you just made **101 queries**.  
That’s the _N+1 problem_ — one main query plus one for each related record.  
It kills performance as your data grows.
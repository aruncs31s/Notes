---
tags:
  - go
cssclasses:
  - wide-page
---
# JSON
- [ ] Check what is marshal and unmarshal.
```go
type SettingResponse struct {
	ID        int       `json:"id"`
	Key       string    `json:"key"`
	JSON      string    `json:"json"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}
```


```go
ID         int       `json:"id" gorm:"column:id;primaryKey"`
```

- This field is an integer (int)
- When serializing to JSON, it will be named "id"
- In the database, it's stored in a column named "id"
- It's configured as the primary key of the table


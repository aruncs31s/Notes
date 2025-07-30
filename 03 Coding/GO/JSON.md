---
tags:
  - go
cssclasses:
  - wide-page
---
# JSON
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


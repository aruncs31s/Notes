---
id: JSON
aliases: []
tags:
  - coding
  - go
cssclasses: 
dg-publish: true
---
# JSON
## Marshal and Unmarshal
- **Marshal**: Convert Go data structures to JSON format.
- **Unmarshal**: Convert JSON data into Go data structures.

```go
package main
import (
	"encoding/json"
	"fmt"
)
type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}
func main() {
	user := User{ID: 1, Name: "SomeOne", Email: "Someone@example.com"}

	// Marshal
	jsonData, err := json.Marshal(user)
	
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}
	fmt.Println("JSON data:", string(jsonData))

	// Unmarshal
	var newUser User
	err = json.Unmarshal(jsonData, &newUser)
	if err != nil {
		fmt.Println("Error unmarshaling JSON:", err)
		return
	}
	fmt.Println("Go struct:", newUser)
}

```

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

## Custom Unmarshal
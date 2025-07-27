---
id: Gin
aliases:
tags:
  - go
---

# Gin

- [[httprouter]]
- https://github.com/julienschmidt/httprouter/blob/master/router.go

## Installation

```bash
go get -u github.com/gin-gonic/gin
```

```bash
import "github.com/gin-gonic/gin"
import "net/http"
```

```go
package main
import "github.com/gin-gonic/gin"
func main() {
  router := gin.Default()
  router.GET("/ping", func(c *gin.Context) {
    c.JSON(200, gin.H{
      "message": "pong",
    })
  })
  router.Run() // listen and serve on 0.0.0.0:8080
}
```

````go
package main
=======
```tasks
path includes 03 Coding/GO/Gin.md
````

- [[Gin CORS]]
  > Install

```bash
go get -u github.com/gin-gonic/gin
```

```go
package main

import (
  "github.com/gin-gonic/gin"
  "net/http"
)
<<<<<<< HEAD
func main() {
  router := gin.Default()
=======

func main() {
  router := gin.Default()
  router.GET("/ping", func(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{
      "message": "pong",
    })
  })
  router.Run() // listen and serve on 0.0.0.0:8080
}
```

#### GET

```go
func main() {
	r := gin.Default()
	r.GET("/ping", controllers.PostCreate)
	r.Run()
}
```

### Creating a post

```go
func PostCreate(c *gin.Context) {
	// TODO:
	// Get data from the req body

	post := models.Post{Title: "Jinzhu", Body: "Just for test"}

	result := initializers.DB.Create(&post) // pass pointer of data to Create
	// Checking for erros
	if result.Error != nil {
		// Bad Request
		c.Status(400)
		return
	}

	fmt.Println(result)
	// create a data post
	c.JSON(http.StatusOK, gin.H{ // same as 200, the jsonify string
		"post":    post,
		"message": "post created successfully",
	})
}
```

router.Run() // listen and serve on 0.0.0.0:8080
}

````

## Config

```go
router.Run() // uses default port or env{PORT}
router.Run("192.168.1.100:8080") // explicit def
router.Run(":8080") // explicit def
````

- [ ] Check what it is

```go
router.SetTrustedProxies([]string{"192.168.1.2"})
```

- [ ] also check proxies
- [ ] also checkout deployment https://gin-gonic.com/en/docs/deployment/



## Reference and Links

1. https://gin-gonic.com/en/docs/learning-resources/

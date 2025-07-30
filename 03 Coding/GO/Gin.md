---
id: Gin
aliases: 
tags:
  - go
cssclasses:
  - wide-page
---

# Gin

- [[httprouter]]
- [[Gin CORS]]
- https://github.com/julienschmidt/httprouter/blob/master/router.go

>[!TODO|right-medium]+Tasks 
> ```tasks
> path includes 03 Coding/GO/Gin.md
> ````

## Installation

```bash
go get -u github.com/gin-gonic/gin
```

```bash
import "github.com/gin-gonic/gin"
import "net/http"
```

## Basics  
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



```go
package main

import (
  "github.com/gin-gonic/gin"
  "net/http"
)
func main() {
  router := gin.Default()

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




## `gin.Cotext`
Context is the most important part of gin. It allows us to pass variables between middleware, manage the flow, validate the JSON of a request and render a JSON response for example


```go
type Context struct {
	Request *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request)
	Writer  [ResponseWriter](https://pkg.go.dev/github.com/gin-gonic/gin?utm_source=godoc#ResponseWriter)
	Params [Params](https://pkg.go.dev/github.com/gin-gonic/gin?utm_source=godoc#Params)
	// Keys is a key/value pair exclusively for the context of each request.
	Keys map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any)

	// Errors is a list of errors attached to all the handlers/middlewares who used this context.
	Errors errorMsgs

	// Accepted defines a list of manually accepted formats for content negotiation.
	Accepted [][string](https://pkg.go.dev/builtin#string)
	// contains filtered or unexported fields
}
```
## Reference and Links

1. https://gin-gonic.com/en/docs/learning-resources/

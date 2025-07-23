---
id: Gin
aliases: []
tags: []
---
# Gin

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

## Config

```go
router.Run() // uses default port or env{PORT}
router.Run("192.168.1.100:8080") // explicit def
router.Run(":8080") // explicit def
```
- [ ] Check what it is 
```go
router.SetTrustedProxies([]string{"192.168.1.2"})
```
## Reference and Links
1. https://gin-gonic.com/en/docs/learning-resources/

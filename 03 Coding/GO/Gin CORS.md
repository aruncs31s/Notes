---
id: Gin CORS
aliases: []
tags:
  - coding
  - go
dg-publish: true
---
# GIN CORS
- [ ] Checkout allowing specific hosts 

```go
import (
  "github.com/gin-contrib/cors"
  "github.com/gin-gonic/gin"
)

func main() {
  router := gin.Default()
  router.Use(cors.Default()) // All origins allowed by default
  router.Run()
}

```

>[!WARNING]
> Allowing all origins disables cookies for clients. For credentialed requests, do not allow all origins.

- [x] pre-flight `OPTIONS` requests. ✅ 2025-07-23

>  It is a small, preliminary request that the browser sends  automatically before sending the actual `HTTP` request
- Before the actual request. 
- Used when these present `PUT`, `DELETE`, `PATCH`, `OPTIONS`

#example 
1. PAUSE: Encounters a complex request 
2.  SEND PRE-FLIGHT:  It sends an OPTIONS request to the same URL

```

Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type

```

3. SERVER RESPONDS: Go server receives this OPTIONS request. And it will 
  * Check if `PUT` and Content-Type are allowed.
  * Respond with a 200 OK status and permission headers:
  * Access-Control-Allow-Origin: https://my-app.com
  * Access-Control-Allow-Methods: GET, POST, PUT, DELETE
* Access-Control-Allow-Headers: Content-Type, Authorization
* It does not runs actual `PUT` command 
* After receiving the response the browser sends the og `PUT` or any request.

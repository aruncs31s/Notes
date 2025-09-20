---
id: HTTP_Servers
aliases: []
tags:
  - coding
  - go
dg-publish: true
---
# HTTP Servers 
## Midlewares 
It sits between  `server` and main `request handler`, it can process the incoming request before  it reaches the business logic and can process after business logic has run.

- Process incoming requests
- Modify request objects
- Terminate requests early
- Modify response objects
- Chain multiple middlewares together

###### Grabing the user agent

```go
userAgent := r.Header.Get("User-Agent")

```

```go
package main

import (
	"fmt"
	"net/http"
)

const validToken = "secret"

// AuthMiddleware checks the "X-Auth-Token" header.
// If it's "secret", call the next handler.
// Otherwise, respond with 401 Unauthorized.
func AuthMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// TODO: Implement the logic:
		//  1) Grab the "X-Auth-Token" header
		//  2) Compare against validToken
		//  3) If mismatch or missing, respond with 401
		//  4) Otherwise pass to next handler
	})
}

// helloHandler returns "Hello!" on GET /hello
func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello!") // INFO: it is a response
}

// secureHandler returns "You are authorized!" on GET /secure
func secureHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "You are authorized!")
}

// SetupServer configures the HTTP routes with the authentication middleware.
func SetupServer() http.Handler {
	mux := http.NewServeMux()

	// Public route: /hello (no auth required)
	mux.HandleFunc("/hello", helloHandler)

	// Secure route: /secure
	// Wrap with AuthMiddleware
	secureRoute := http.HandlerFunc(secureHandler)
	mux.Handle("/secure", AuthMiddleware(secureRoute))

	return mux
}

func main() {
	// Optional: you can run a real server for local testing
	http.ListenAndServe(":8090", SetupServer())
}

```

-  `w http.ResponseWriter` -> This is an interface that the server uses to write the HTTP response back to the client.
- `r *http.Request` -> This represents the incoming HTTP request from the client. It contains information like the request URL, headers, and body.

```go
type HandlerFunc func(ResponseWriter, *Request)
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
    f(w, r)
}

```

```go
// Basic middleware structure
func middleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        // Logic before the handler
        fmt.Println("Before handler")
        
        // Call the next handler
        next.ServeHTTP(w, r)
        
        // Logic after the handler
        fmt.Println("After handler")
    })
}

```


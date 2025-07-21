# HTTP Servers 
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


# GO CORS
```go
import (
    "github.com/rs/cors"
    "net/http"
)
func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/articles", handleArticles)
    
    // Configure CORS
    c := cors.New(cors.Options{
        AllowedOrigins:   []string{"http://localhost:3000", "https://myapp.com"},
        AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
        AllowedHeaders:   []string{"*"},
        AllowCredentials: true,
    })
    
    handler := c.Handler(mux)
    
    log.Println("Server starting on :8080")
    log.Fatal(http.ListenAndServe(":8080", handler))
}
```

- [x] pre-flight `OPTIONS` requests. ✅ 2025-07-23

>  It is a small, preliminary request that the browser sends  automatically before sending the actual `HTTP` request
- Before the actual request. 

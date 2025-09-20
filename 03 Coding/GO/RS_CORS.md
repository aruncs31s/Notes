---
id: RS_CORS
aliases: []
tags:
  - coding
  - go
dg-publish: true
---
# RS/CORS 

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


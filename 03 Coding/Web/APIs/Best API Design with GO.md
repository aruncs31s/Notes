---
id: Best_API_Design_with_GO
aliases: []
tags:
  - coding
  - web
  - apis
dg-publish: true
---
# Best REST API Design with GO

## Table of Contents
1. [Project Structure](#project-structure)
2. [Router Setup](#router-setup)
3. [Middleware](#middleware)
4. [Handler Patterns](#handler-patterns)
5. [Data Models & Validation](#data-models--validation)
6. [Database Integration](#database-integration)
7. [Error Handling](#error-handling)
8. [Authentication & Authorization](#authentication--authorization)
9. [Security & Safety Concerns](#security--safety-concerns)
10. [Testing](#testing)
11. [Documentation](#documentation)
12. [Performance & Monitoring](#performance--monitoring)

## Project Structure

### Recommended Directory Layout

```

project/
├── cmd/
│   └── api/
│       └── main.go
├── internal/
│   ├── handlers/
│   │   ├── user.go
│   │   ├── auth.go
│   │   └── middleware.go
│   ├── models/
│   │   ├── user.go
│   │   └── response.go
│   ├── repository/
│   │   ├── user_repo.go
│   │   └── interface.go
│   ├── service/
│   │   └── user_service.go
│   └── config/
│       └── config.go
├── pkg/
│   ├── database/
│   │   └── connection.go
│   └── utils/
│       └── validator.go
├── api/
│   └── openapi.yaml
├── docker-compose.yml
├── Dockerfile
├── go.mod
└── go.sum

```

## Router Setup with Gin Framework

### Why Choose Gin?

**Gin** is a high-performance HTTP web framework written in Go. It's designed to be fast, minimalist, and feature-rich, making it an excellent choice for building REST APIs. Here's why Gin stands out:

- **Performance**: Gin is one of the fastest Go web frameworks, with minimal memory footprint
- **Middleware Support**: Rich ecosystem of middleware for common tasks (CORS, authentication, logging)
- **JSON Binding**: Built-in support for binding JSON, XML, and form data to structs
- **Route Grouping**: Clean organization of routes with nested groups
- **Easy Testing**: Simple testing framework with built-in test mode

### Basic Gin Setup

The basic setup demonstrates fundamental Gin concepts including middleware, routing, and server configuration.

```go
package main

import (
    "log"
    "net/http"
    "time"
    
    "github.com/gin-gonic/gin"
    "github.com/gin-contrib/cors"
)

func main() {
    // Set Gin mode - controls logging and performance optimizations
    // Options: gin.DebugMode, gin.ReleaseMode, gin.TestMode
    gin.SetMode(gin.ReleaseMode)
    
    // Create new Gin router instance
    // gin.New() creates a clean router without default middleware
    // gin.Default() includes Logger and Recovery middleware
    r := gin.New()
    
    // Built-in middleware
    r.Use(gin.Logger())    // Logs HTTP requests in a specific format
    r.Use(gin.Recovery())  // Recovers from panics and returns 500 status
    
    // CORS (Cross-Origin Resource Sharing) middleware
    // Essential for web applications that make requests from browsers
    config := cors.DefaultConfig()
    config.AllowOrigins = []string{"http://localhost:3000", "https://yourdomain.com"}
    config.AllowMethods = []string{"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"}
    config.AllowHeaders = []string{"Origin", "Content-Type", "Accept", "Authorization"}
    config.AllowCredentials = true  // Allow cookies and authorization headers
    r.Use(cors.New(config))
    
    // Custom middleware - executed in order for every request
    r.Use(RequestIDMiddleware())  // Adds unique ID to each request
    r.Use(LoggingMiddleware())    // Custom logging format
    
    // API versioning using route groups
    // Groups allow you to organize routes and apply middleware to specific routes
    v1 := r.Group("/api/v1")
    {
        // Health check endpoint - essential for monitoring and load balancers
        v1.GET("/health", HealthCheck)
        
        // User routes grouped together for better organization
        users := v1.Group("/users")
        {
            users.GET("", GetUsers)          // GET /api/v1/users
            users.POST("", CreateUser)       // POST /api/v1/users
            users.GET("/:id", GetUser)       // GET /api/v1/users/123
            users.PUT("/:id", UpdateUser)    // PUT /api/v1/users/123 (full update)
            users.PATCH("/:id", PatchUser)   // PATCH /api/v1/users/123 (partial update)
            users.DELETE("/:id", DeleteUser) // DELETE /api/v1/users/123
        }
        
        // Authentication routes - public endpoints
        auth := v1.Group("/auth")
        {
            auth.POST("/login", Login)                    // User login
            auth.POST("/register", Register)              // User registration
            auth.POST("/refresh", RefreshToken)           // Token refresh
            auth.POST("/logout", AuthMiddleware(), Logout) // Logout (requires auth)
        }
        
        // Protected routes - require authentication
        // All routes in this group will have AuthMiddleware applied
        protected := v1.Group("/")
        protected.Use(AuthMiddleware())
        {
            protected.GET("/profile", GetProfile)      // Get current user profile
            protected.PUT("/profile", UpdateProfile)   // Update current user profile
        }
    }
    
    // Custom server configuration for production
    server := &http.Server{
        Addr:           ":8080",
        Handler:        r,
        ReadTimeout:    10 * time.Second,  // Time to read request
        WriteTimeout:   10 * time.Second,  // Time to write response
        MaxHeaderBytes: 1 << 20,           // 1 MB max header size
    }
    
    log.Println("Server starting on :8080")
    log.Fatal(server.ListenAndServe())
}

// Custom middleware examples with detailed explanations

// RequestIDMiddleware adds a unique identifier to each request
// This is crucial for debugging, logging, and request tracing
func RequestIDMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Check if client provided a request ID
        requestID := c.GetHeader("X-Request-ID")
        if requestID == "" {
            // Generate a new request ID if not provided
            requestID = generateRequestID()
        }
        
        // Store in context for use in handlers
        c.Set("request_id", requestID)
        
        // Return in response headers for client tracking
        c.Header("X-Request-ID", requestID)
        
        // Continue to next middleware/handler
        c.Next()
    }
}

// LoggingMiddleware provides custom request logging format
// More flexible than gin.Logger() for specific logging needs
func LoggingMiddleware() gin.HandlerFunc {
    return gin.LoggerWithFormatter(func(param gin.LogFormatterParams) string {
        // Custom log format with essential information
        return fmt.Sprintf("%s - [%s] \"%s %s %s %d %s \"%s\" %s\"\n",
            param.ClientIP,                    // Client IP address
            param.TimeStamp.Format(time.RFC1123), // Request timestamp
            param.Method,                      // HTTP method
            param.Path,                        // Request path
            param.Request.Proto,               // HTTP protocol version
            param.StatusCode,                  // Response status code
            param.Latency,                     // Request processing time
            param.Request.UserAgent(),         // Client user agent
            param.ErrorMessage,                // Error message if any
        )
    })
}

// generateRequestID creates a unique identifier for request tracking
func generateRequestID() string {
    // Simple implementation using nanosecond timestamp
    // In production, consider using UUID or more sophisticated ID generation
    return fmt.Sprintf("%d", time.Now().UnixNano())
}

```

**Key Concepts Explained:**

1. **Gin Modes**: Control behavior for different environments
   - `DebugMode`: Verbose logging, helpful for development
   - `ReleaseMode`: Optimized for production, minimal logging
   - `TestMode`: Used during testing, disables console output

2. **Middleware Chain**: Functions that run before/after request handlers
   - Execute in the order they're registered
   - Can modify request/response or terminate the chain
   - Use `c.Next()` to continue or `c.Abort()` to stop

3. **Route Groups**: Organize related routes and apply middleware selectively
   - Nested groups inherit parent middleware
   - Clean URL structure with common prefixes
   - Easy to version APIs (/api/v1, /api/v2)

4. **HTTP Methods & REST Conventions**:
   - `GET`: Retrieve resources (idempotent, no side effects)
   - `POST`: Create new resources
   - `PUT`: Update entire resource (idempotent)
   - `PATCH`: Partial update of resource
   - `DELETE`: Remove resource (idempotent)

### Advanced Gin Setup with Dependency Injection

This pattern demonstrates a more scalable architecture using dependency injection and separation of concerns.

```go
package main

import (
    "database/sql"
    "log"
    "net/http"
    "time"
    
    "github.com/gin-gonic/gin"
    "github.com/gin-contrib/cors"
    
    "your-project/internal/config"
    "your-project/internal/handlers"
    "your-project/internal/middleware"
    "your-project/internal/repository"
    "your-project/internal/service"
    "your-project/pkg/database"
)

// Server struct encapsulates all application dependencies
// This promotes dependency injection and makes testing easier
type Server struct {
    router      *gin.Engine           // HTTP router
    db          *sql.DB               // Database connection
    config      *config.Config        // Application configuration
    userHandler *handlers.UserHandler // User-related HTTP handlers
    authHandler *handlers.AuthHandler // Authentication HTTP handlers
}

// NewServer creates a new server instance with all dependencies
// This is the dependency injection pattern - all dependencies are injected here
func NewServer(cfg *config.Config) (*Server, error) {
    // Database connection with connection pooling
    db, err := database.NewConnection(cfg.DatabaseURL)
    if err != nil {
        return nil, err
    }
    
    // Repository layer - handles data persistence
    // This layer abstracts database operations from business logic
    userRepo := repository.NewPostgresUserRepo(db)
    
    // Service layer - contains business logic
    // Services use repositories to perform business operations
    userService := service.NewUserService(userRepo)
    authService := service.NewAuthService(userRepo, cfg.JWTSecret)
    
    // Handler layer - HTTP request/response handling
    // Handlers use services to process HTTP requests
    userHandler := handlers.NewUserHandler(userService)
    authHandler := handlers.NewAuthHandler(authService)
    
    // Create server instance with all dependencies
    server := &Server{
        db:          db,
        config:      cfg,
        userHandler: userHandler,
        authHandler: authHandler,
    }
    
    // Setup router with all routes and middleware
    server.setupRouter()
    return server, nil
}

// setupRouter configures all routes and middleware
// Separated from NewServer for better organization
func (s *Server) setupRouter() {
    // Set Gin mode based on environment configuration
    if s.config.Environment == "production" {
        gin.SetMode(gin.ReleaseMode)
    }
    
    r := gin.New()
    
    // Global middleware applied to all routes
    // Order matters - middleware executes in the order added
    r.Use(gin.Recovery())              // Panic recovery
    r.Use(middleware.Logger())         // Custom logging
    r.Use(middleware.CORS())           // Cross-origin requests
    r.Use(middleware.RequestID())      // Request tracking
    r.Use(middleware.RateLimit())      // Rate limiting protection
    
    // API versioning group
    api := r.Group("/api/v1")
    
    // Public routes - no authentication required
    api.GET("/health", s.healthCheck)
    api.POST("/auth/login", s.authHandler.Login)
    api.POST("/auth/register", s.authHandler.Register)
    
    // Protected routes - authentication required
    // All routes in this group will have Auth middleware applied
    protected := api.Group("/")
    protected.Use(middleware.Auth(s.config.JWTSecret))
    {
        // User management routes
        users := protected.Group("/users")
        {
            users.GET("", s.userHandler.GetUsers)
            users.GET("/:id", s.userHandler.GetUser)
            users.PUT("/:id", s.userHandler.UpdateUser)
            users.DELETE("/:id", s.userHandler.DeleteUser)
        }
        
        // Profile management routes
        protected.GET("/profile", s.userHandler.GetProfile)
        protected.PUT("/profile", s.userHandler.UpdateProfile)
    }
    
    s.router = r
}

// Start begins serving HTTP requests
func (s *Server) Start() error {
    server := &http.Server{
        Addr:    ":" + s.config.Port,
        Handler: s.router,
    }
    
    log.Printf("Server starting on port %s", s.config.Port)
    return server.ListenAndServe()
}

// healthCheck is a simple health check endpoint
// Essential for load balancers and monitoring systems
func (s *Server) healthCheck(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{
        "status": "healthy",
        "time":   time.Now(),
    })
}

```

**Architecture Benefits Explained:**

1. **Dependency Injection**: All dependencies are injected at startup
   - Makes testing easier (can inject mock dependencies)
   - Promotes loose coupling between components
   - Clear dependency graph

2. **Layered Architecture**:
   - **Handler Layer**: HTTP concerns (request/response parsing)
   - **Service Layer**: Business logic and validation
   - **Repository Layer**: Data access and persistence
   - **Clean separation of responsibilities**

3. **Configuration Management**: Centralized configuration
   - Environment-based settings
   - Easy to modify for different deployments
   - Secure handling of secrets

### Gin Middleware Deep Dive

Middleware in Gin provides a powerful way to handle cross-cutting concerns. Here are production-ready middleware examples with detailed explanations.

```go
package middleware

import (
    "fmt"
    "net/http"
    "strconv"
    "strings"
    "time"
    
    "github.com/gin-gonic/gin"
    "github.com/golang-jwt/jwt/v4"
    "golang.org/x/time/rate"
)

// CORS Middleware - Handles Cross-Origin Resource Sharing
// Essential for web applications that make requests from browsers to different domains
func CORS() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Get the origin from the request header
        origin := c.Request.Header.Get("Origin")
        
        // Set CORS headers to allow cross-origin requests
        c.Writer.Header().Set("Access-Control-Allow-Origin", origin)
        c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
        c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
        c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT, PATCH, DELETE")

        // Handle preflight requests (OPTIONS method)
        // Browsers send OPTIONS requests before actual requests to check permissions
        if c.Request.Method == "OPTIONS" {
            c.AbortWithStatus(http.StatusNoContent)
            return
        }

        // Continue to next middleware or handler
        c.Next()
    }
}

// Authentication Middleware - Validates JWT tokens
// Protects routes that require user authentication
func Auth(secret string) gin.HandlerFunc {
    return func(c *gin.Context) {
        // Get Authorization header from request
        authHeader := c.GetHeader("Authorization")
        if authHeader == "" {
            c.JSON(http.StatusUnauthorized, gin.H{
                "error": "Authorization header required",
            })
            c.Abort() // Stop middleware chain execution
            return
        }
        
        // Extract token from "Bearer <token>" format
        tokenString := strings.TrimPrefix(authHeader, "Bearer ")
        if tokenString == authHeader {
            // Header doesn't contain "Bearer " prefix
            c.JSON(http.StatusUnauthorized, gin.H{
                "error": "Bearer token required",
            })
            c.Abort()
            return
        }
        
        // Parse and validate JWT token
        token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
            // Verify signing method is HMAC
            if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
                return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
            }
            return []byte(secret), nil
        })
        
        // Check for parsing errors or invalid token
        if err != nil || !token.Valid {
            c.JSON(http.StatusUnauthorized, gin.H{
                "error": "Invalid token",
            })
            c.Abort()
            return
        }
        
        // Extract claims from valid token
        claims, ok := token.Claims.(jwt.MapClaims)
        if !ok {
            c.JSON(http.StatusUnauthorized, gin.H{
                "error": "Invalid token claims",
            })
            c.Abort()
            return
        }
        
        // Store user information in context for use in handlers
        c.Set("user_id", claims["user_id"])
        c.Set("email", claims["email"])
        
        // Continue to next middleware or handler
        c.Next()
    }
}

// Rate Limiting Middleware - Protects against abuse and DDoS
// Implements token bucket algorithm for rate limiting
func RateLimit() gin.HandlerFunc {
    // Create rate limiter: 10 requests per second with burst of 20
    limiter := rate.NewLimiter(10, 20)
    
    return func(c *gin.Context) {
        // Check if request is allowed by rate limiter
        if !limiter.Allow() {
            c.JSON(http.StatusTooManyRequests, gin.H{
                "error": "Rate limit exceeded",
            })
            c.Abort()
            return
        }
        c.Next()
    }
}

// Advanced Rate Limiting with per-IP limits
func PerIPRateLimit() gin.HandlerFunc {
    // Map to store rate limiters for each IP
    limiters := make(map[string]*rate.Limiter)
    mu := &sync.RWMutex{}
    
    return func(c *gin.Context) {
        ip := c.ClientIP()
        
        // Get or create limiter for this IP
        mu.RLock()
        limiter, exists := limiters[ip]
        mu.RUnlock()
        
        if !exists {
            // Create new limiter for this IP
            limiter = rate.NewLimiter(5, 10) // 5 requests/second, burst 10
            mu.Lock()
            limiters[ip] = limiter
            mu.Unlock()
        }
        
        if !limiter.Allow() {
            c.JSON(http.StatusTooManyRequests, gin.H{
                "error": "Rate limit exceeded for your IP",
            })
            c.Abort()
            return
        }
        
        c.Next()
    }
}

// Request ID Middleware - Adds unique identifier to each request
// Critical for debugging, logging, and distributed tracing
func RequestID() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Check if client provided request ID
        requestID := c.GetHeader("X-Request-ID")
        if requestID == "" {
            // Generate unique request ID using nanosecond timestamp
            requestID = fmt.Sprintf("%d", time.Now().UnixNano())
        }
        
        // Store in context for use throughout request lifecycle
        c.Set("request_id", requestID)
        
        // Return in response headers for client tracking
        c.Header("X-Request-ID", requestID)
        c.Next()
    }
}

// Custom Logger Middleware - Enhanced logging with colors and formatting
// Provides detailed request information for monitoring and debugging
func Logger() gin.HandlerFunc {
    return gin.LoggerWithFormatter(func(param gin.LogFormatterParams) string {
        var statusColor, methodColor, resetColor string
        
        // Add colors for console output (disabled in production)
        if param.IsOutputColor() {
            statusColor = param.StatusCodeColor()
            methodColor = param.MethodColor()
            resetColor = param.ResetColor()
        }

        // Truncate very long latencies for readability
        if param.Latency > time.Minute {
            param.Latency = param.Latency.Truncate(time.Second)
        }

        // Format log entry with essential information
        return fmt.Sprintf("[GIN] %v |%s %3d %s| %13v | %15s |%s %-7s %s %#v\n%s",
            param.TimeStamp.Format("2006/01/02 - 15:04:05"), // Timestamp
            statusColor, param.StatusCode, resetColor,         // Status code with color
            param.Latency,                                     // Request processing time
            param.ClientIP,                                    // Client IP address
            methodColor, param.Method, resetColor,             // HTTP method with color
            param.Path,                                        // Request path
            param.ErrorMessage,                                // Error message if any
        )
    })
}

// Error Handler Middleware - Centralized error handling
// Catches errors from handlers and formats consistent error responses
func ErrorHandler() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Execute next middleware/handler and capture any errors
        c.Next()
        
        // Check if any errors were added to the context
        if len(c.Errors) > 0 {
            err := c.Errors.Last() // Get the last error
            
            // Handle different types of errors differently
            switch err.Type {
            case gin.ErrorTypeBind:
                // JSON binding or validation error
                c.JSON(http.StatusBadRequest, gin.H{
                    "error": "Invalid request format",
                    "details": err.Error(),
                })
            case gin.ErrorTypePublic:
                // Public error that can be shown to client
                c.JSON(http.StatusInternalServerError, gin.H{
                    "error": "Internal server error",
                })
            default:
                // Generic error handling
                c.JSON(http.StatusInternalServerError, gin.H{
                    "error": "Something went wrong",
                })
            }
        }
    }
}

// Timeout Middleware - Prevents requests from hanging indefinitely
// Essential for maintaining server responsiveness under load
func Timeout(timeout time.Duration) gin.HandlerFunc {
    return func(c *gin.Context) {
        // Create context with timeout
        ctx, cancel := context.WithTimeout(c.Request.Context(), timeout)
        defer cancel() // Always call cancel to free resources
        
        // Replace request context with timeout context
        c.Request = c.Request.WithContext(ctx)
        
        // Channel to signal completion
        finished := make(chan struct{})
        panicChan := make(chan interface{}, 1)
        
        // Execute handler in goroutine
        go func() {
            defer func() {
                if p := recover(); p != nil {
                    panicChan <- p
                }
            }()
            
            c.Next()           // Execute handler
            finished <- struct{}{} // Signal completion
        }()
        
        // Wait for completion, panic, or timeout
        select {
        case <-finished:
            // Handler completed successfully
            return
        case p := <-panicChan:
            // Handler panicked, re-panic to trigger recovery middleware
            panic(p)
        case <-ctx.Done():
            // Timeout occurred
            c.JSON(http.StatusRequestTimeout, gin.H{
                "error": "Request timeout",
            })
            c.Abort()
        }
    }
}

// Security Headers Middleware - Adds security-related HTTP headers
func SecurityHeaders() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Prevent content type sniffing
        c.Header("X-Content-Type-Options", "nosniff")
        
        // Prevent clickjacking attacks
        c.Header("X-Frame-Options", "DENY")
        
        // Enable XSS protection
        c.Header("X-XSS-Protection", "1; mode=block")
        
        // Enforce HTTPS (only in production)
        c.Header("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
        
        // Content Security Policy
        c.Header("Content-Security-Policy", "default-src 'self'")
        
        c.Next()
    }
}

```

**Middleware Concepts Explained:**

1. **Execution Order**: Middleware executes in the order it's registered
   - Request flows down through middleware chain
   - Response flows back up through middleware chain
   - Use `c.Next()` to continue or `c.Abort()` to stop

2. **Context Usage**: Store and retrieve data using `c.Set()` and `c.Get()`
   - Share data between middleware and handlers
   - Store user info, request IDs, database connections

3. **Error Handling**: Different approaches for error management
   - Return errors immediately with `c.JSON()` and `c.Abort()`
   - Add errors to context with `c.Error()` for centralized handling

4. **Security Considerations**:
   - Rate limiting prevents abuse
   - CORS enables secure cross-origin requests
   - Security headers protect against common attacks
   - Authentication ensures only authorized access

## Gin Handler Patterns and Response Management

Handlers in Gin are responsible for processing HTTP requests and returning appropriate responses. Here are production-ready patterns with comprehensive explanations.

```go
package middleware

import (
    "log"
    "net/http"
    "time"
)

func LoggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        
        // Create a response writer wrapper to capture status code
        wrapper := &responseWriter{ResponseWriter: w, statusCode: http.StatusOK}
        
        next.ServeHTTP(wrapper, r)
        
        log.Printf("%s %s %d %v", 
            r.Method, 
            r.URL.Path, 
            wrapper.statusCode, 
            time.Since(start))
    })
}

type responseWriter struct {
    http.ResponseWriter
    statusCode int
}

func (rw *responseWriter) WriteHeader(code int) {
    rw.statusCode = code
    rw.ResponseWriter.WriteHeader(code)
}

```

### Authentication Middleware

```go
package middleware

import (
    "context"
    "net/http"
    "strings"
    
    "github.com/golang-jwt/jwt/v4"
)

func AuthMiddleware(secret []byte) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            authHeader := r.Header.Get("Authorization")
            if authHeader == "" {
                http.Error(w, "Authorization header required", http.StatusUnauthorized)
                return
            }
            
            tokenString := strings.TrimPrefix(authHeader, "Bearer ")
            
            token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
                return secret, nil
            })
            
            if err != nil || !token.Valid {
                http.Error(w, "Invalid token", http.StatusUnauthorized)
                return
            }
            
            claims := token.Claims.(jwt.MapClaims)
            userID := claims["user_id"].(string)
            
            // Add user ID to context
            ctx := context.WithValue(r.Context(), "user_id", userID)
            next.ServeHTTP(w, r.WithContext(ctx))
        })
    }
}

```

### Rate Limiting Middleware

```go
package middleware

import (
    "net/http"
    "sync"
    "time"
    
    "golang.org/x/time/rate"
)

type RateLimiter struct {
    visitors map[string]*rate.Limiter
    mu       sync.RWMutex
    rate     rate.Limit
    burst    int
}

func NewRateLimiter(r rate.Limit, b int) *RateLimiter {
    return &RateLimiter{
        visitors: make(map[string]*rate.Limiter),
        rate:     r,
        burst:    b,
    }
}

func (rl *RateLimiter) getLimiter(ip string) *rate.Limiter {
    rl.mu.Lock()
    defer rl.mu.Unlock()
    
    limiter, exists := rl.visitors[ip]
    if !exists {
        limiter = rate.NewLimiter(rl.rate, rl.burst)
        rl.visitors[ip] = limiter
    }
    
    return limiter
}

func (rl *RateLimiter) Middleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        ip := r.RemoteAddr
        limiter := rl.getLimiter(ip)
        
        if !limiter.Allow() {
            http.Error(w, "Rate limit exceeded", http.StatusTooManyRequests)
            return
        }
        
        next.ServeHTTP(w, r)
    })
}

```

### Gin Response Helpers - Standardized API Responses

Consistent response formatting is crucial for API usability. These helpers ensure all endpoints return responses in the same format.

```go
package handlers

import (
    "net/http"
    "time"
    
    "github.com/gin-gonic/gin"
)

// Standard response structure for Gin
type GinResponse struct {
    Success   bool        `json:"success"`
    Data      interface{} `json:"data,omitempty"`
    Error     *APIError   `json:"error,omitempty"`
    Meta      *Meta       `json:"meta"`
}

type APIError struct {
    Code    string      `json:"code"`
    Message string      `json:"message"`
    Details interface{} `json:"details,omitempty"`
}

type Meta struct {
    Timestamp time.Time `json:"timestamp"`
    RequestID string    `json:"request_id,omitempty"`
}

// Success response helper
func Success(c *gin.Context, status int, data interface{}) {
    requestID, _ := c.Get("request_id")
    
    response := GinResponse{
        Success: true,
        Data:    data,
        Meta: &Meta{
            Timestamp: time.Now(),
            RequestID: requestID.(string),
        },
    }
    
    c.JSON(status, response)
}

// Error response helper
func Error(c *gin.Context, status int, code, message string, details interface{}) {
    requestID, _ := c.Get("request_id")
    
    response := GinResponse{
        Success: false,
        Error: &APIError{
            Code:    code,
            Message: message,
            Details: details,
        },
        Meta: &Meta{
            Timestamp: time.Now(),
            RequestID: requestID.(string),
        },
    }
    
    c.JSON(status, response)
}

// Validation error helper
func ValidationError(c *gin.Context, errors interface{}) {
    Error(c, http.StatusBadRequest, "VALIDATION_ERROR", "Validation failed", errors)
}

// Not found helper
func NotFound(c *gin.Context, resource string) {
    Error(c, http.StatusNotFound, "NOT_FOUND", resource+" not found", nil)
}

// Internal error helper
func InternalError(c *gin.Context, message string) {
    Error(c, http.StatusInternalServerError, "INTERNAL_ERROR", message, nil)
}

```

### User Handler with Gin

```go
package handlers

import (
    "net/http"
    "strconv"
    
    "github.com/gin-gonic/gin"
    "your-project/internal/models"
    "your-project/internal/service"
)

type UserHandler struct {
    userService service.UserService
}

func NewUserHandler(userService service.UserService) *UserHandler {
    return &UserHandler{
        userService: userService,
    }
}

// GET /api/v1/users
func (h *UserHandler) GetUsers(c *gin.Context) {
    // Parse query parameters
    page, _ := strconv.Atoi(c.DefaultQuery("page", "1"))
    if page < 1 {
        page = 1
    }
    
    limit, _ := strconv.Atoi(c.DefaultQuery("limit", "20"))
    if limit < 1 || limit > 100 {
        limit = 20
    }
    
    // Optional filters
    status := c.Query("status")
    search := c.Query("search")
    
    users, total, err := h.userService.GetUsers(page, limit, status, search)
    if err != nil {
        InternalError(c, "Failed to retrieve users")
        return
    }
    
    response := gin.H{
        "users": users,
        "pagination": gin.H{
            "page":       page,
            "limit":      limit,
            "total":      total,
            "total_pages": (total + limit - 1) / limit,
            "has_next":   page*limit < total,
            "has_prev":   page > 1,
        },
    }
    
    Success(c, http.StatusOK, response)
}

// POST /api/v1/users
func (h *UserHandler) CreateUser(c *gin.Context) {
    var req models.CreateUserRequest
    
    if err := c.ShouldBindJSON(&req); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    // Validate using custom validator
    if err := req.Validate(); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    user, err := h.userService.CreateUser(&req)
    if err != nil {
        if err == service.ErrUserExists {
            Error(c, http.StatusConflict, "USER_EXISTS", "User already exists", nil)
            return
        }
        InternalError(c, "Failed to create user")
        return
    }
    
    Success(c, http.StatusCreated, user)
}

// GET /api/v1/users/:id
func (h *UserHandler) GetUser(c *gin.Context) {
    id, err := strconv.Atoi(c.Param("id"))
    if err != nil {
        Error(c, http.StatusBadRequest, "INVALID_ID", "Invalid user ID", nil)
        return
    }
    
    user, err := h.userService.GetUser(id)
    if err != nil {
        if err == service.ErrUserNotFound {
            NotFound(c, "User")
            return
        }
        InternalError(c, "Failed to retrieve user")
        return
    }
    
    Success(c, http.StatusOK, user)
}

// PUT /api/v1/users/:id
func (h *UserHandler) UpdateUser(c *gin.Context) {
    id, err := strconv.Atoi(c.Param("id"))
    if err != nil {
        Error(c, http.StatusBadRequest, "INVALID_ID", "Invalid user ID", nil)
        return
    }
    
    var req models.UpdateUserRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    // Check authorization - users can only update their own profile
    userID, exists := c.Get("user_id")
    if !exists || userID != strconv.Itoa(id) {
        Error(c, http.StatusForbidden, "FORBIDDEN", "Cannot update other user's profile", nil)
        return
    }
    
    user, err := h.userService.UpdateUser(id, &req)
    if err != nil {
        if err == service.ErrUserNotFound {
            NotFound(c, "User")
            return
        }
        InternalError(c, "Failed to update user")
        return
    }
    
    Success(c, http.StatusOK, user)
}

// PATCH /api/v1/users/:id
func (h *UserHandler) PatchUser(c *gin.Context) {
    id, err := strconv.Atoi(c.Param("id"))
    if err != nil {
        Error(c, http.StatusBadRequest, "INVALID_ID", "Invalid user ID", nil)
        return
    }
    
    // For PATCH, we accept partial updates
    var updates map[string]interface{}
    if err := c.ShouldBindJSON(&updates); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    user, err := h.userService.PatchUser(id, updates)
    if err != nil {
        if err == service.ErrUserNotFound {
            NotFound(c, "User")
            return
        }
        InternalError(c, "Failed to update user")
        return
    }
    
    Success(c, http.StatusOK, user)
}

// DELETE /api/v1/users/:id
func (h *UserHandler) DeleteUser(c *gin.Context) {
    id, err := strconv.Atoi(c.Param("id"))
    if err != nil {
        Error(c, http.StatusBadRequest, "INVALID_ID", "Invalid user ID", nil)
        return
    }
    
    err = h.userService.DeleteUser(id)
    if err != nil {
        if err == service.ErrUserNotFound {
            NotFound(c, "User")
            return
        }
        InternalError(c, "Failed to delete user")
        return
    }
    
    c.JSON(http.StatusNoContent, nil)
}

// GET /api/v1/profile
func (h *UserHandler) GetProfile(c *gin.Context) {
    userID, exists := c.Get("user_id")
    if !exists {
        Error(c, http.StatusUnauthorized, "UNAUTHORIZED", "User not authenticated", nil)
        return
    }
    
    id, _ := strconv.Atoi(userID.(string))
    user, err := h.userService.GetUser(id)
    if err != nil {
        InternalError(c, "Failed to retrieve profile")
        return
    }
    
    Success(c, http.StatusOK, user)
}

```

### Authentication Handler with Gin

```go
package handlers

import (
    "net/http"
    "time"
    
    "github.com/gin-gonic/gin"
    "golang.org/x/crypto/bcrypt"
    "your-project/internal/auth"
    "your-project/internal/models"
    "your-project/internal/service"
)

type AuthHandler struct {
    userService service.UserService
    jwtSecret   string
}

type LoginRequest struct {
    Email    string `json:"email" binding:"required,email"`
    Password string `json:"password" binding:"required"`
}

type RegisterRequest struct {
    Name     string `json:"name" binding:"required,min=2,max=50"`
    Email    string `json:"email" binding:"required,email"`
    Password string `json:"password" binding:"required,min=8"`
}

type LoginResponse struct {
    Token        string       `json:"token"`
    RefreshToken string       `json:"refresh_token"`
    User         *models.User `json:"user"`
    ExpiresAt    time.Time    `json:"expires_at"`
}

func NewAuthHandler(userService service.UserService, jwtSecret string) *AuthHandler {
    return &AuthHandler{
        userService: userService,
        jwtSecret:   jwtSecret,
    }
}

// POST /api/v1/auth/login
func (h *AuthHandler) Login(c *gin.Context) {
    var req LoginRequest
    
    if err := c.ShouldBindJSON(&req); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    user, err := h.userService.GetUserByEmail(req.Email)
    if err != nil {
        Error(c, http.StatusUnauthorized, "INVALID_CREDENTIALS", 
            "Invalid email or password", nil)
        return
    }
    
    if err := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(req.Password)); err != nil {
        Error(c, http.StatusUnauthorized, "INVALID_CREDENTIALS", 
            "Invalid email or password", nil)
        return
    }
    
    // Generate tokens
    token, expiresAt, err := auth.GenerateToken(user.ID, user.Email, h.jwtSecret)
    if err != nil {
        InternalError(c, "Failed to generate token")
        return
    }
    
    refreshToken, err := auth.GenerateRefreshToken(user.ID, h.jwtSecret)
    if err != nil {
        InternalError(c, "Failed to generate refresh token")
        return
    }
    
    user.Password = "" // Don't return password
    
    response := LoginResponse{
        Token:        token,
        RefreshToken: refreshToken,
        User:         user,
        ExpiresAt:    expiresAt,
    }
    
    Success(c, http.StatusOK, response)
}

// POST /api/v1/auth/register
func (h *AuthHandler) Register(c *gin.Context) {
    var req RegisterRequest
    
    if err := c.ShouldBindJSON(&req); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    // Hash password
    hashedPassword, err := bcrypt.GenerateFromPassword([]byte(req.Password), bcrypt.DefaultCost)
    if err != nil {
        InternalError(c, "Failed to process password")
        return
    }
    
    user := &models.User{
        Name:     req.Name,
        Email:    req.Email,
        Password: string(hashedPassword),
    }
    
    createdUser, err := h.userService.CreateUser(user)
    if err != nil {
        if err == service.ErrUserExists {
            Error(c, http.StatusConflict, "USER_EXISTS", "User already exists", nil)
            return
        }
        InternalError(c, "Failed to create user")
        return
    }
    
    Success(c, http.StatusCreated, createdUser)
}

// POST /api/v1/auth/refresh
func (h *AuthHandler) RefreshToken(c *gin.Context) {
    var req struct {
        RefreshToken string `json:"refresh_token" binding:"required"`
    }
    
    if err := c.ShouldBindJSON(&req); err != nil {
        ValidationError(c, err.Error())
        return
    }
    
    claims, err := auth.ValidateRefreshToken(req.RefreshToken, h.jwtSecret)
    if err != nil {
        Error(c, http.StatusUnauthorized, "INVALID_TOKEN", "Invalid refresh token", nil)
        return
    }
    
    // Generate new access token
    newToken, expiresAt, err := auth.GenerateToken(claims.UserID, claims.Email, h.jwtSecret)
    if err != nil {
        InternalError(c, "Failed to generate new token")
        return
    }
    
    response := gin.H{
        "token":      newToken,
        "expires_at": expiresAt,
    }
    
    Success(c, http.StatusOK, response)
}

// POST /api/v1/auth/logout
func (h *AuthHandler) Logout(c *gin.Context) {
    // In a real application, you might want to blacklist the token
    // or store it in a revoked tokens list
    
    Success(c, http.StatusOK, gin.H{
        "message": "Successfully logged out",
    })
}

```

## Security & Safety Concerns

Security is paramount when building REST APIs. This section covers critical security considerations and implementation strategies to protect your Gin-based API from common vulnerabilities and attacks.

### 1. Input Validation & Sanitization

**Why Critical**: Malicious input is the #1 attack vector for web applications. Proper validation prevents injection attacks, data corruption, and unexpected behavior.

#### Comprehensive Input Validation Strategy

```go
package security

import (
    "html"
    "regexp"
    "strings"
    "unicode"
    
    "github.com/gin-gonic/gin"
)

// SanitizeInput removes potentially dangerous characters from user input
func SanitizeInput(input string) string {
    // Remove HTML tags and encode HTML entities
    sanitized := html.EscapeString(input)
    
    // Remove null bytes and control characters
    sanitized = strings.ReplaceAll(sanitized, "\x00", "")
    
    // Trim whitespace
    sanitized = strings.TrimSpace(sanitized)
    
    return sanitized
}

// ValidateAndSanitizeMiddleware applies input sanitization to all requests
func ValidateAndSanitizeMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Sanitize URL parameters
        for _, param := range c.Params {
            param.Value = SanitizeInput(param.Value)
        }
        
        // Sanitize query parameters
        queryValues := c.Request.URL.Query()
        for key, values := range queryValues {
            for i, value := range values {
                queryValues[key][i] = SanitizeInput(value)
            }
        }
        c.Request.URL.RawQuery = queryValues.Encode()
        
        c.Next()
    }
}

// XSS Protection - Validate that input doesn't contain script tags
func ValidateNoXSS(input string) bool {
    // Check for common XSS patterns
    xssPatterns := []string{
        `<script`,
        `javascript:`,
        `onload=`,
        `onerror=`,
        `onclick=`,
        `eval\(`,
    }
    
    lowerInput := strings.ToLower(input)
    for _, pattern := range xssPatterns {
        if strings.Contains(lowerInput, pattern) {
            return false
        }
    }
    return true
}

// SQL Injection Prevention - Additional validation for database inputs
func ValidateNoSQLInjection(input string) bool {
    // Common SQL injection patterns
    sqlPatterns := []string{
        `'.*--`,
        `'.*#`,
        `union.*select`,
        `drop.*table`,
        `insert.*into`,
        `delete.*from`,
        `exec\(`,
        `sp_`,
    }
    
    lowerInput := strings.ToLower(input)
    for _, pattern := range sqlPatterns {
        matched, _ := regexp.MatchString(pattern, lowerInput)
        if matched {
            return false
        }
    }
    return true
}

// File Upload Security
func ValidateFileUpload(filename string, maxSize int64, allowedTypes []string) error {
    // Check file extension
    ext := strings.ToLower(filepath.Ext(filename))
    allowed := false
    for _, allowedType := range allowedTypes {
        if ext == allowedType {
            allowed = true
            break
        }
    }
    if !allowed {
        return errors.New("file type not allowed")
    }
    
    // Additional security checks would include:
    // - File content validation (not just extension)
    // - Virus scanning
    // - File size limits
    // - Filename sanitization
    
    return nil
}

```

### 2. Authentication & Authorization Security

#### Secure JWT Implementation

```go
package auth

import (
    "crypto/rand"
    "encoding/base64"
    "errors"
    "time"
    
    "github.com/golang-jwt/jwt/v4"
    "golang.org/x/crypto/bcrypt"
)

// Secure JWT configuration
const (
    // Use strong secrets in production (32+ bytes)
    MinSecretLength = 32
    // Short token lifetime reduces exposure window
    AccessTokenLifetime  = 15 * time.Minute
    RefreshTokenLifetime = 7 * 24 * time.Hour
    // Strong password hashing cost
    BcryptCost = 12
)

// Claims structure with security considerations
type Claims struct {
    UserID   string `json:"user_id"`
    Email    string `json:"email"`
    Role     string `json:"role"`
    TokenID  string `json:"token_id"` // For token revocation
    IsRefresh bool   `json:"is_refresh,omitempty"`
    jwt.RegisteredClaims
}

// GenerateSecureToken creates JWT with security best practices
func GenerateSecureToken(userID, email, role, secret string) (string, time.Time, error) {
    // Validate secret strength
    if len(secret) < MinSecretLength {
        return "", time.Time{}, errors.New("JWT secret too weak")
    }
    
    // Generate unique token ID for revocation capability
    tokenID, err := generateRandomString(16)
    if err != nil {
        return "", time.Time{}, err
    }
    
    expirationTime := time.Now().Add(AccessTokenLifetime)
    
    claims := &Claims{
        UserID:  userID,
        Email:   email,
        Role:    role,
        TokenID: tokenID,
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(expirationTime),
            IssuedAt:  jwt.NewNumericDate(time.Now()),
            NotBefore: jwt.NewNumericDate(time.Now()),
            Issuer:    "your-api-name",
            Subject:   userID,
        },
    }
    
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    tokenString, err := token.SignedString([]byte(secret))
    
    return tokenString, expirationTime, err
}

// ValidateToken with comprehensive security checks
func ValidateToken(tokenString, secret string) (*Claims, error) {
    token, err := jwt.ParseWithClaims(tokenString, &Claims{}, func(token *jwt.Token) (interface{}, error) {
        // Verify the signing method
        if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
            return nil, errors.New("invalid signing method")
        }
        return []byte(secret), nil
    })
    
    if err != nil {
        return nil, err
    }
    
    claims, ok := token.Claims.(*Claims)
    if !ok || !token.Valid {
        return nil, errors.New("invalid token")
    }
    
    // Additional security checks
    if claims.IsRefresh {
        return nil, errors.New("refresh token cannot be used for authentication")
    }
    
    // Check if token is in blacklist (implement token revocation)
    if IsTokenBlacklisted(claims.TokenID) {
        return nil, errors.New("token has been revoked")
    }
    
    return claims, nil
}

// Secure password hashing
func HashPassword(password string) (string, error) {
    // Use high cost for production
    bytes, err := bcrypt.GenerateFromPassword([]byte(password), BcryptCost)
    return string(bytes), err
}

// generateRandomString for secure token IDs
func generateRandomString(length int) (string, error) {
    bytes := make([]byte, length)
    if _, err := rand.Read(bytes); err != nil {
        return "", err
    }
    return base64.URLEncoding.EncodeToString(bytes), nil
}

// Token revocation system (simple in-memory implementation)
var blacklistedTokens = make(map[string]time.Time)
var blacklistMutex sync.RWMutex

func BlacklistToken(tokenID string, expiry time.Time) {
    blacklistMutex.Lock()
    defer blacklistMutex.Unlock()
    blacklistedTokens[tokenID] = expiry
}

func IsTokenBlacklisted(tokenID string) bool {
    blacklistMutex.RLock()
    defer blacklistMutex.RUnlock()
    
    expiry, exists := blacklistedTokens[tokenID]
    if !exists {
        return false
    }
    
    // Clean up expired blacklisted tokens
    if time.Now().After(expiry) {
        delete(blacklistedTokens, tokenID)
        return false
    }
    
    return true
}

```

### 3. HTTPS & TLS Security

```go
package server

import (
    "crypto/tls"
    "net/http"
    "time"
)

// SecureServerConfig provides production-ready TLS configuration
func SecureServerConfig(certFile, keyFile string) *http.Server {
    // TLS configuration with security best practices
    tlsConfig := &tls.Config{
        MinVersion:               tls.VersionTLS12, // Minimum TLS 1.2
        CurvePreferences:         []tls.CurveID{tls.CurveP521, tls.CurveP384, tls.CurveP256},
        PreferServerCipherSuites: true,
        CipherSuites: []uint16{
            tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
            tls.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,
            tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
        },
    }
    
    server := &http.Server{
        Addr:         ":443",
        TLSConfig:    tlsConfig,
        ReadTimeout:  10 * time.Second,
        WriteTimeout: 10 * time.Second,
        IdleTimeout:  30 * time.Second,
    }
    
    return server
}

// HTTPS Redirect Middleware
func HTTPSRedirectMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        if c.Request.Header.Get("X-Forwarded-Proto") != "https" {
            httpsURL := "https://" + c.Request.Host + c.Request.RequestURI
            c.Redirect(http.StatusMovedPermanently, httpsURL)
            return
        }
        c.Next()
    }
}

```

### 4. Rate Limiting & DDoS Protection

```go
package security

import (
    "sync"
    "time"
    
    "github.com/gin-gonic/gin"
    "golang.org/x/time/rate"
)

// Advanced Rate Limiting with different limits for different endpoints
type RateLimitConfig struct {
    RequestsPerSecond rate.Limit
    BurstSize        int
    WindowSize       time.Duration
}

var (
    // Different limits for different endpoint types
    PublicEndpointLimit = RateLimitConfig{
        RequestsPerSecond: 10,
        BurstSize:        20,
        WindowSize:       time.Minute,
    }
    
    AuthEndpointLimit = RateLimitConfig{
        RequestsPerSecond: 2,   // Stricter for auth endpoints
        BurstSize:        5,
        WindowSize:       time.Minute,
    }
    
    APIEndpointLimit = RateLimitConfig{
        RequestsPerSecond: 50,
        BurstSize:        100,
        WindowSize:       time.Minute,
    }
)

// IP-based rate limiter with cleanup
type IPRateLimiter struct {
    limiters map[string]*rate.Limiter
    mu       sync.RWMutex
    config   RateLimitConfig
    lastSeen map[string]time.Time
}

func NewIPRateLimiter(config RateLimitConfig) *IPRateLimiter {
    limiter := &IPRateLimiter{
        limiters: make(map[string]*rate.Limiter),
        lastSeen: make(map[string]time.Time),
        config:   config,
    }
    
    // Cleanup goroutine to remove old entries
    go limiter.cleanup()
    
    return limiter
}

func (rl *IPRateLimiter) GetLimiter(ip string) *rate.Limiter {
    rl.mu.Lock()
    defer rl.mu.Unlock()
    
    limiter, exists := rl.limiters[ip]
    if !exists {
        limiter = rate.NewLimiter(rl.config.RequestsPerSecond, rl.config.BurstSize)
        rl.limiters[ip] = limiter
    }
    
    rl.lastSeen[ip] = time.Now()
    return limiter
}

func (rl *IPRateLimiter) cleanup() {
    ticker := time.NewTicker(time.Hour)
    defer ticker.Stop()
    
    for range ticker.C {
        rl.mu.Lock()
        cutoff := time.Now().Add(-2 * time.Hour)
        
        for ip, lastSeen := range rl.lastSeen {
            if lastSeen.Before(cutoff) {
                delete(rl.limiters, ip)
                delete(rl.lastSeen, ip)
            }
        }
        rl.mu.Unlock()
    }
}

// Suspicious Activity Detection
func SuspiciousActivityMiddleware() gin.HandlerFunc {
    suspiciousPatterns := []string{
        `\.\.\/`,                    // Directory traversal
        `<script`,                   // XSS attempts
        `union.*select`,             // SQL injection
        `exec\(`,                    // Code injection
        `/admin`,                    // Admin path scanning
        `/wp-admin`,                 // WordPress scanning
        `phpMyAdmin`,                // Database tool scanning
    }
    
    return func(c *gin.Context) {
        requestPath := strings.ToLower(c.Request.URL.Path)
        userAgent := strings.ToLower(c.Request.UserAgent())
        
        // Check for suspicious patterns
        for _, pattern := range suspiciousPatterns {
            if matched, _ := regexp.MatchString(pattern, requestPath); matched {
                LogSuspiciousActivity(c.ClientIP(), "suspicious_path", requestPath)
                c.JSON(http.StatusForbidden, gin.H{"error": "Access denied"})
                c.Abort()
                return
            }
        }
        
        // Check for bot-like behavior
        if strings.Contains(userAgent, "bot") || strings.Contains(userAgent, "crawler") {
            // Implement stricter rate limiting for bots
            c.Header("X-Robots-Tag", "noindex, nofollow")
        }
        
        c.Next()
    }
}

func LogSuspiciousActivity(ip, activityType, details string) {
    // Log to security monitoring system
    log.Printf("SECURITY ALERT: IP %s - %s - %s", ip, activityType, details)
    // In production, send to SIEM or security monitoring service
}

```

### 5. Database Security

```go
package database

import (
    "database/sql"
    "fmt"
    
    _ "github.com/lib/pq"
)

// Secure database connection with proper configuration
func NewSecureConnection(dbURL string) (*sql.DB, error) {
    // Add SSL mode and other security parameters
    secureURL := fmt.Sprintf("%s?sslmode=require&connect_timeout=10", dbURL)
    
    db, err := sql.Open("postgres", secureURL)
    if err != nil {
        return nil, err
    }
    
    // Configure connection pool for security and performance
    db.SetMaxOpenConns(25)                 // Limit connections
    db.SetMaxIdleConns(5)                  // Limit idle connections
    db.SetConnMaxLifetime(5 * time.Minute) // Rotate connections
    
    return db, db.Ping()
}

// Prepared statement helper to prevent SQL injection
func SafeQuery(db *sql.DB, query string, args ...interface{}) (*sql.Rows, error) {
    // Always use prepared statements
    stmt, err := db.Prepare(query)
    if err != nil {
        return nil, err
    }
    defer stmt.Close()
    
    return stmt.Query(args...)
}

// Database audit logging
func LogDatabaseOperation(userID, operation, table string) {
    log.Printf("DB_AUDIT: User %s performed %s on %s at %s", 
        userID, operation, table, time.Now().Format(time.RFC3339))
}

```

### 6. Error Handling Security

```go
package handlers

import (
    "log"
    "github.com/gin-gonic/gin"
)

// Secure error handling that doesn't leak sensitive information
func SecureErrorHandler() gin.HandlerFunc {
    return func(c *gin.Context) {
        c.Next()
        
        if len(c.Errors) > 0 {
            err := c.Errors.Last()
            
            // Log detailed error for debugging (server-side only)
            log.Printf("ERROR: %s %s - %v", c.Request.Method, c.Request.URL.Path, err)
            
            // Return generic error to client (don't expose internal details)
            switch err.Type {
            case gin.ErrorTypeBind:
                c.JSON(http.StatusBadRequest, gin.H{
                    "error": "Invalid request format",
                    "code":  "INVALID_REQUEST",
                })
            case gin.ErrorTypePublic:
                c.JSON(http.StatusInternalServerError, gin.H{
                    "error": "Internal server error",
                    "code":  "INTERNAL_ERROR",
                })
            default:
                c.JSON(http.StatusInternalServerError, gin.H{
                    "error": "Something went wrong",
                    "code":  "UNKNOWN_ERROR",
                })
            }
        }
    }
}

// Don't expose sensitive information in error messages
func SafeError(c *gin.Context, status int, publicMessage string, internalError error) {
    // Log detailed error internally
    log.Printf("Internal error: %v", internalError)
    
    // Return only safe information to client
    c.JSON(status, gin.H{
        "error": publicMessage,
        "code":  http.StatusText(status),
    })
}

```

### 7. Security Headers & CORS

```go
package middleware

func SecurityHeadersMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        // Prevent content type sniffing
        c.Header("X-Content-Type-Options", "nosniff")
        
        // Prevent clickjacking
        c.Header("X-Frame-Options", "DENY")
        
        // Enable XSS protection
        c.Header("X-XSS-Protection", "1; mode=block")
        
        // HSTS for HTTPS enforcement
        c.Header("Strict-Transport-Security", "max-age=31536000; includeSubDomains; preload")
        
        // Content Security Policy
        c.Header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'")
        
        // Referrer Policy
        c.Header("Referrer-Policy", "strict-origin-when-cross-origin")
        
        // Remove server information
        c.Header("Server", "")
        
        c.Next()
    }
}

// Secure CORS configuration
func SecureCORSMiddleware() gin.HandlerFunc {
    return cors.New(cors.Config{
        AllowOrigins: []string{
            "https://yourdomain.com",
            "https://app.yourdomain.com",
            // Never use "*" in production
        },
        AllowMethods: []string{
            "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS",
        },
        AllowHeaders: []string{
            "Origin", "Content-Type", "Accept", "Authorization",
            "X-Requested-With", "X-CSRF-Token",
        },
        ExposeHeaders: []string{
            "X-Request-ID",
        },
        AllowCredentials: true,
        MaxAge:          12 * time.Hour,
    })
}

```

### 8. Security Monitoring & Logging

```go
package monitoring

import (
    "context"
    "log"
    "time"
    
    "github.com/gin-gonic/gin"
)

// Security event types
const (
    EventFailedLogin     = "failed_login"
    EventSuspiciousIP    = "suspicious_ip"
    EventRateLimitHit    = "rate_limit_exceeded"
    EventInvalidToken    = "invalid_token"
    EventSQLInjection    = "sql_injection_attempt"
    EventXSSAttempt      = "xss_attempt"
)

type SecurityEvent struct {
    Type        string    `json:"type"`
    IP          string    `json:"ip"`
    UserAgent   string    `json:"user_agent"`
    Path        string    `json:"path"`
    UserID      string    `json:"user_id,omitempty"`
    Details     string    `json:"details"`
    Timestamp   time.Time `json:"timestamp"`
    Severity    string    `json:"severity"`
}

// Security monitoring middleware
func SecurityMonitoringMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        start := time.Now()
        
        c.Next()
        
        // Monitor for security events based on response
        if c.Writer.Status() == http.StatusUnauthorized {
            LogSecurityEvent(SecurityEvent{
                Type:      EventInvalidToken,
                IP:        c.ClientIP(),
                UserAgent: c.Request.UserAgent(),
                Path:      c.Request.URL.Path,
                Timestamp: time.Now(),
                Severity:  "medium",
            })
        }
        
        if c.Writer.Status() == http.StatusTooManyRequests {
            LogSecurityEvent(SecurityEvent{
                Type:      EventRateLimitHit,
                IP:        c.ClientIP(),
                UserAgent: c.Request.UserAgent(),
                Path:      c.Request.URL.Path,
                Timestamp: time.Now(),
                Severity:  "high",
            })
        }
        
        // Log slow requests (potential DoS)
        duration := time.Since(start)
        if duration > 5*time.Second {
            LogSecurityEvent(SecurityEvent{
                Type:      "slow_request",
                IP:        c.ClientIP(),
                Path:      c.Request.URL.Path,
                Details:   fmt.Sprintf("Request took %v", duration),
                Timestamp: time.Now(),
                Severity:  "medium",
            })
        }
    }
}

func LogSecurityEvent(event SecurityEvent) {
    // Log to file/database
    log.Printf("SECURITY_EVENT: %+v", event)
    
    // In production, send to SIEM or security monitoring service
    // Example: send to Elasticsearch, Splunk, or security API
    
    // For high severity events, consider immediate alerting
    if event.Severity == "high" {
        AlertSecurityTeam(event)
    }
}

func AlertSecurityTeam(event SecurityEvent) {
    // Send immediate alert via email, Slack, PagerDuty, etc.
    log.Printf("HIGH SEVERITY SECURITY EVENT: %+v", event)
}

```

### 9. Production Security Checklist

#### Environment Configuration

```bash
# Environment variables for production
export GIN_MODE=release
export JWT_SECRET="your-super-long-random-secret-at-least-32-characters"
export DB_SSL_MODE=require
export ALLOWED_ORIGINS="https://yourdomain.com,https://app.yourdomain.com"
export RATE_LIMIT_REQUESTS_PER_SECOND=10
export BCRYPT_COST=12

```

#### Security Best Practices Summary

1. **Authentication & Authorization**:
   - Use strong JWT secrets (32+ characters)
   - Implement token rotation and revocation
   - Use HTTPS everywhere
   - Hash passwords with bcrypt (cost 12+)

2. **Input Validation**:
   - Validate all inputs server-side
   - Sanitize user inputs
   - Use parameterized queries
   - Implement file upload restrictions

3. **Rate Limiting & DDoS Protection**:
   - Implement per-IP rate limiting
   - Use different limits for different endpoints
   - Monitor for suspicious patterns
   - Log security events

4. **Network Security**:
   - Use HTTPS with strong TLS configuration
   - Implement proper CORS policies
   - Add security headers
   - Hide server information

5. **Error Handling**:
   - Don't expose internal errors to clients
   - Log detailed errors server-side
   - Use generic error messages
   - Implement proper status codes

6. **Database Security**:
   - Use SSL connections
   - Implement connection limits
   - Use prepared statements
   - Audit database operations

7. **Monitoring & Logging**:
   - Log all security events
   - Monitor for suspicious activity
   - Implement alerting for high-severity events
   - Regular security audits

**Remember**: Security is an ongoing process, not a one-time setup. Regularly update dependencies, monitor for vulnerabilities, and conduct security audits.

## Testing Your API with cURL Commands

This section provides comprehensive cURL examples for testing every endpoint in your Gin REST API. These commands are essential for development, testing, and API documentation.

### Environment Setup

First, set up environment variables for easier testing:

```bash
# Base URL for your API
export API_BASE="http://localhost:8080/api/v1"

# For HTTPS in production
export API_BASE="https://yourdomain.com/api/v1"

# JWT token (will be set after login)
export TOKEN=""

```

### 1. Health Check Endpoint

**Purpose**: Verify that the API server is running and healthy.

```bash
# Basic health check
curl -X GET "${API_BASE}/health" \
  -H "Content-Type: application/json" \
  -w "\nResponse Time: %{time_total}s\nHTTP Code: %{http_code}\n"

# Expected Response:
# {
#   "success": true,
#   "data": {
#     "status": "healthy",
#     "time": "2025-08-02T10:30:00Z"
#   },
#   "meta": {
#     "timestamp": "2025-08-02T10:30:00Z",
#     "request_id": "1722598200000000000"
#   }
# }

```

### 2. Authentication Endpoints

#### User Registration

```bash
# Register a new user
curl -X POST "${API_BASE}/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "SecurePass123!"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (201 Created):
# {
#   "success": true,
#   "data": {
#     "id": 1,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "created_at": "2025-08-02T10:30:00Z"
#   },
#   "meta": {
#     "timestamp": "2025-08-02T10:30:00Z",
#     "request_id": "1722598200000000001"
#   }
# }

```

#### User Login

```bash
# Login and get JWT token
curl -X POST "${API_BASE}/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePass123!"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#     "user": {
#       "id": 1,
#       "name": "John Doe",
#       "email": "john.doe@example.com"
#     },
#     "expires_at": "2025-08-02T10:45:00Z"
#   }
# }

# Extract token for subsequent requests
export TOKEN=$(curl -s -X POST "${API_BASE}/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "john.doe@example.com", "password": "SecurePass123!"}' | \
  jq -r '.data.token')

```

#### Token Refresh

```bash
# Refresh JWT token
curl -X POST "${API_BASE}/auth/refresh" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#     "expires_at": "2025-08-02T11:00:00Z"
#   }
# }

```

#### User Logout

```bash
# Logout (requires authentication)
curl -X POST "${API_BASE}/auth/logout" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${TOKEN}" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "message": "Successfully logged out"
#   }
# }

```

### 3. User Management Endpoints

#### Get All Users (with Pagination)

```bash
# Get users with default pagination
curl -X GET "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Get users with custom pagination and filters
curl -X GET "${API_BASE}/users?page=1&limit=10&status=active&search=john" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "users": [
#       {
#         "id": 1,
#         "name": "John Doe",
#         "email": "john.doe@example.com",
#         "status": "active",
#         "created_at": "2025-08-02T10:30:00Z"
#       }
#     ],
#     "pagination": {
#       "page": 1,
#       "limit": 10,
#       "total": 1,
#       "total_pages": 1,
#       "has_next": false,
#       "has_prev": false
#     }
#   }
# }

```

#### Get Specific User

```bash
# Get user by ID
curl -X GET "${API_BASE}/users/1" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "id": 1,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "status": "active",
#     "created_at": "2025-08-02T10:30:00Z",
#     "updated_at": "2025-08-02T10:30:00Z"
#   }
# }

# User not found (404)
curl -X GET "${API_BASE}/users/999" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (404 Not Found):
# {
#   "success": false,
#   "error": {
#     "code": "NOT_FOUND",
#     "message": "User not found"
#   }
# }

```

#### Create New User (Admin Only)

```bash
# Create new user
curl -X POST "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "password": "SecurePass456!",
    "age": 28,
    "role": "user"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (201 Created):
# {
#   "success": true,
#   "data": {
#     "id": 2,
#     "name": "Jane Smith",
#     "email": "jane.smith@example.com",
#     "age": 28,
#     "role": "user",
#     "status": "active",
#     "created_at": "2025-08-02T10:35:00Z"
#   }
# }

# Validation error example
curl -X POST "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "A",
    "email": "invalid-email",
    "password": "123"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (400 Bad Request):
# {
#   "success": false,
#   "error": {
#     "code": "VALIDATION_ERROR",
#     "message": "Validation failed",
#     "details": [
#       "name must be at least 2 characters",
#       "Invalid email format",
#       "password must be at least 8 characters"
#     ]
#   }
# }

```

#### Update User (Full Update - PUT)

```bash
# Full user update
curl -X PUT "${API_BASE}/users/1" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Updated",
    "age": 30
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "id": 1,
#     "name": "John Updated",
#     "email": "john.doe@example.com",
#     "age": 30,
#     "updated_at": "2025-08-02T10:40:00Z"
#   }
# }

# Forbidden access (trying to update another user)
curl -X PUT "${API_BASE}/users/2" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"name": "Unauthorized Update"}' \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (403 Forbidden):
# {
#   "success": false,
#   "error": {
#     "code": "FORBIDDEN",
#     "message": "Cannot update other user's profile"
#   }
# }

```

#### Partial Update (PATCH)

```bash
# Partial user update
curl -X PATCH "${API_BASE}/users/1" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Partially Updated"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

# Update multiple fields
curl -X PATCH "${API_BASE}/users/1" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Final",
    "age": 32,
    "status": "inactive"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

```

#### Delete User

```bash
# Delete user
curl -X DELETE "${API_BASE}/users/2" \
  -H "Authorization: Bearer ${TOKEN}" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (204 No Content):
# No response body for successful deletion

# Try to delete non-existent user
curl -X DELETE "${API_BASE}/users/999" \
  -H "Authorization: Bearer ${TOKEN}" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (404 Not Found):
# {
#   "success": false,
#   "error": {
#     "code": "NOT_FOUND",
#     "message": "User not found"
#   }
# }

```

### 4. Profile Management Endpoints

#### Get Current User Profile

```bash
# Get current user's profile
curl -X GET "${API_BASE}/profile" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (200 OK):
# {
#   "success": true,
#   "data": {
#     "id": 1,
#     "name": "John Final",
#     "email": "john.doe@example.com",
#     "age": 32,
#     "status": "active",
#     "created_at": "2025-08-02T10:30:00Z",
#     "updated_at": "2025-08-02T10:45:00Z"
#   }
# }

```

#### Update Current User Profile

```bash
# Update current user's profile
curl -X PUT "${API_BASE}/profile" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Profile Updated",
    "age": 33
  }' \
  -w "\nHTTP Code: %{http_code}\n"

```

### 5. Error Handling Examples

#### Authentication Errors

```bash
# Request without token
curl -X GET "${API_BASE}/users" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (401 Unauthorized):
# {
#   "error": "Authorization header required"
# }

# Request with invalid token
curl -X GET "${API_BASE}/users" \
  -H "Authorization: Bearer invalid_token_here" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (401 Unauthorized):
# {
#   "error": "Invalid token"
# }

# Request with malformed Bearer token
curl -X GET "${API_BASE}/users" \
  -H "Authorization: InvalidFormat token_here" \
  -H "Content-Type: application/json" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (401 Unauthorized):
# {
#   "error": "Bearer token required"
# }

```

#### Rate Limiting

```bash
# Test rate limiting (make multiple rapid requests)
for i in {1..25}; do
  curl -X GET "${API_BASE}/health" \
    -H "Content-Type: application/json" \
    -w "Request $i: %{http_code}\n" \
    -s -o /dev/null
done

# After hitting rate limit (429 Too Many Requests):
# {
#   "error": "Rate limit exceeded"
# }

```

### 6. Advanced Testing Scenarios

#### File Upload (if implemented)

```bash
# Upload file with proper validation
curl -X POST "${API_BASE}/users/1/avatar" \
  -H "Authorization: Bearer ${TOKEN}" \
  -F "file=@/path/to/image.jpg" \
  -w "\nHTTP Code: %{http_code}\n"

# Upload invalid file type
curl -X POST "${API_BASE}/users/1/avatar" \
  -H "Authorization: Bearer ${TOKEN}" \
  -F "file=@/path/to/document.pdf" \
  -w "\nHTTP Code: %{http_code}\n"

```

#### Content-Type Validation

```bash
# Send invalid content type
curl -X POST "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: text/plain" \
  -d "This is not JSON" \
  -w "\nHTTP Code: %{http_code}\n"

# Expected Response (400 Bad Request):
# {
#   "success": false,
#   "error": {
#     "code": "VALIDATION_ERROR",
#     "message": "Invalid request format"
#   }
# }

```

#### CORS Testing

```bash
# Test CORS preflight request
curl -X OPTIONS "${API_BASE}/users" \
  -H "Origin: https://yourdomain.com" \
  -H "Access-Control-Request-Method: GET" \
  -H "Access-Control-Request-Headers: Authorization" \
  -w "\nHTTP Code: %{http_code}\n"

# Check CORS headers in response
curl -X GET "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Origin: https://yourdomain.com" \
  -I \
  -w "\nHTTP Code: %{http_code}\n"

```

### 7. Performance Testing

#### Load Testing with curl

```bash
# Simple load test script
#!/bin/bash
echo "Starting load test..."
for i in {1..100}; do
  (curl -s -X GET "${API_BASE}/health" \
    -w "%{time_total}\n" \
    -o /dev/null) &
done
wait
echo "Load test completed"

# Measure response times
curl -X GET "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -w "DNS Lookup: %{time_namelookup}s\nConnect: %{time_connect}s\nSSL: %{time_appconnect}s\nTime to First Byte: %{time_starttransfer}s\nTotal Time: %{time_total}s\n" \
  -o /dev/null

```

### 8. Automation Scripts

#### Complete User Workflow Test

```bash
#!/bin/bash
# Complete user workflow test script

API_BASE="http://localhost:8080/api/v1"

echo "=== API Workflow Test ==="

# 1. Health check
echo "1. Testing health endpoint..."
curl -s -X GET "${API_BASE}/health" | jq '.'

# 2. Register user
echo "2. Registering new user..."
REGISTER_RESPONSE=$(curl -s -X POST "${API_BASE}/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "password": "TestPass123!"
  }')
echo $REGISTER_RESPONSE | jq '.'

# 3. Login user
echo "3. Logging in user..."
LOGIN_RESPONSE=$(curl -s -X POST "${API_BASE}/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "TestPass123!"
  }')

TOKEN=$(echo $LOGIN_RESPONSE | jq -r '.data.token')
echo "Token obtained: ${TOKEN:0:20}..."

# 4. Get profile
echo "4. Getting user profile..."
curl -s -X GET "${API_BASE}/profile" \
  -H "Authorization: Bearer ${TOKEN}" | jq '.'

# 5. Update profile
echo "5. Updating user profile..."
curl -s -X PUT "${API_BASE}/profile" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Test User",
    "age": 25
  }' | jq '.'

# 6. Logout
echo "6. Logging out user..."
curl -s -X POST "${API_BASE}/auth/logout" \
  -H "Authorization: Bearer ${TOKEN}" | jq '.'

echo "=== Workflow test completed ==="

```

### 9. Environment-Specific Examples

#### Development Environment

```bash
# Development with detailed output
export API_BASE="http://localhost:8080/api/v1"
export CURL_OPTS="-v -w \nHTTP Code: %{http_code}\nResponse Time: %{time_total}s\n"

# Development login with debug info
curl ${CURL_OPTS} -X POST "${API_BASE}/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "dev@example.com", "password": "devpass"}'

```

#### Production Environment

```bash
# Production with minimal output and error handling
export API_BASE="https://api.yourdomain.com/api/v1"
export CURL_OPTS="-s -f --retry 3 --retry-delay 1"

# Production health check with retry
curl ${CURL_OPTS} "${API_BASE}/health" || echo "API is down!"

```

### 10. Security Testing

#### SQL Injection Attempts

```bash
# Test SQL injection protection
curl -X POST "${API_BASE}/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@example.com'\''OR 1=1--",
    "password": "anything"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

```

#### XSS Attempts

```bash
# Test XSS protection
curl -X POST "${API_BASE}/users" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "<script>alert(\"XSS\")</script>",
    "email": "test@example.com",
    "password": "password123"
  }' \
  -w "\nHTTP Code: %{http_code}\n"

```

### Key Testing Strategies:

1. **Authentication Flow**: Always test the complete auth workflow
2. **Error Scenarios**: Test all error conditions and edge cases  
3. **Input Validation**: Verify all validation rules work correctly
4. **Authorization**: Ensure users can only access authorized resources
5. **Rate Limiting**: Test that rate limiting works as expected
6. **CORS**: Verify cross-origin requests work properly
7. **Performance**: Measure response times under load
8. **Security**: Test for common vulnerabilities

These cURL examples provide a comprehensive testing framework for your Gin REST API, covering all endpoints, error scenarios, and security considerations.

## Gin Validation & Binding - Input Validation Made Easy

Gin provides powerful built-in validation using struct tags and the validator package. This ensures data integrity and provides clear error messages to clients.

### Why Validation Matters

1. **Security**: Prevents malicious input from reaching your business logic
2. **Data Integrity**: Ensures only valid data enters your system
3. **User Experience**: Provides clear feedback about invalid input
4. **Code Quality**: Reduces validation logic scattered throughout handlers

### Gin Built-in Validation

Gin uses the `go-playground/validator` package for validation, which provides comprehensive validation rules through struct tags.

```go
package models

import (
    "github.com/gin-gonic/gin/binding"
    "github.com/go-playground/validator/v10"
)

// User request models with comprehensive Gin validation tags
type CreateUserRequest struct {
    Name     string `json:"name" binding:"required,min=2,max=50"`              // Required, 2-50 characters
    Email    string `json:"email" binding:"required,email"`                    // Required, valid email format
    Password string `json:"password" binding:"required,min=8"`                 // Required, minimum 8 characters
    Age      int    `json:"age" binding:"required,min=18,max=120"`            // Required, 18-120 years old
    Role     string `json:"role" binding:"required,oneof=user admin"`          // Must be "user" or "admin"
}

type UpdateUserRequest struct {
    Name string `json:"name" binding:"omitempty,min=2,max=50"`               // Optional, but if provided, 2-50 chars
    Age  int    `json:"age" binding:"omitempty,min=18,max=120"`             // Optional, but if provided, 18-120
}

// Advanced validation with custom error handling
func ValidateUserRequest(c *gin.Context) {
    var req CreateUserRequest
    
    // ShouldBindJSON automatically validates based on struct tags
    if err := c.ShouldBindJSON(&req); err != nil {
        var validationErrors []string
        
        // Check if error is validation error
        if errs, ok := err.(validator.ValidationErrors); ok {
            // Process each validation error
            for _, e := range errs {
                switch e.Tag() {
                case "required":
                    validationErrors = append(validationErrors, e.Field()+" is required")
                case "email":
                    validationErrors = append(validationErrors, "Invalid email format")
                case "min":
                    validationErrors = append(validationErrors, fmt.Sprintf("%s must be at least %s characters", e.Field(), e.Param()))
                case "max":
                    validationErrors = append(validationErrors, fmt.Sprintf("%s must be at most %s characters", e.Field(), e.Param()))
                case "oneof":
                    validationErrors = append(validationErrors, e.Field()+" must be one of the allowed values")
                default:
                    validationErrors = append(validationErrors, e.Field()+" is invalid")
                }
            }
        } else {
            // Handle JSON parsing errors
            validationErrors = append(validationErrors, "Invalid JSON format")
        }
        
        c.JSON(http.StatusBadRequest, gin.H{
            "error": "Validation failed",
            "details": validationErrors,
        })
        return
    }
    
    // Validation passed, continue processing
    // ... rest of handler logic
}

// Common validation tags explained:
// - required: Field must be present and not empty
// - omitempty: Skip validation if field is empty
// - min/max: Minimum/maximum length for strings, value for numbers
// - email: Valid email format
// - url: Valid URL format
// - oneof: Value must be one of specified options
// - gt/gte: Greater than / greater than or equal
// - lt/lte: Less than / less than or equal
// - len: Exact length
// - alpha: Alphabetic characters only
// - alphanum: Alphanumeric characters only
// - numeric: Numeric characters only

```

**Validation Benefits:**

1. **Automatic Validation**: Gin automatically validates based on struct tags
2. **Comprehensive Rules**: Wide variety of built-in validation rules
3. **Error Details**: Detailed error information for debugging
4. **Performance**: Fast validation with minimal overhead

### Custom Validators for Gin

Sometimes you need validation rules specific to your business logic. Custom validators provide this flexibility.

```go
package validators

import (
    "regexp"
    
    "github.com/go-playground/validator/v10"
)

// RegisterCustomValidators sets up all custom validation rules
// Call this once during application initialization
func RegisterCustomValidators() {
    // Get the validator instance from Gin's binding engine
    if v, ok := binding.Validator.Engine().(*validator.Validate); ok {
        // Register each custom validator with a tag name
        v.RegisterValidation("strongpassword", validateStrongPassword)
        v.RegisterValidation("username", validateUsername)
        v.RegisterValidation("phonenumber", validatePhoneNumber)
    }
}

// validateStrongPassword ensures password meets security requirements
// Business rule: password must have uppercase, lowercase, digit, and special character
func validateStrongPassword(fl validator.FieldLevel) bool {
    password := fl.Field().String()
    
    // Check minimum length
    if len(password) < 8 {
        return false
    }
    
    // Regex patterns for different character types
    hasUpper := regexp.MustCompile(`[A-Z]`).MatchString(password)
    hasLower := regexp.MustCompile(`[a-z]`).MatchString(password)
    hasDigit := regexp.MustCompile(`\d`).MatchString(password)
    hasSpecial := regexp.MustCompile(`[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]`).MatchString(password)
    
    // All criteria must be met
    return hasUpper && hasLower && hasDigit && hasSpecial
}

// validateUsername ensures username follows naming conventions
// Business rule: alphanumeric with underscores, 3-20 characters
func validateUsername(fl validator.FieldLevel) bool {
    username := fl.Field().String()
    
    // Check against regex pattern
    matched, _ := regexp.MatchString(`^[a-zA-Z0-9_]{3,20}$`, username)
    return matched
}

// validatePhoneNumber checks for valid phone number format
// Supports various international formats
func validatePhoneNumber(fl validator.FieldLevel) bool {
    phone := fl.Field().String()
    
    // Regex for international phone numbers
    phoneRegex := regexp.MustCompile(`^\+?[1-9]\d{1,14}$`)
    return phoneRegex.MatchString(phone)
}

// Usage in model structs
type UserRegistration struct {
    Username string `json:"username" binding:"required,username"`           // Uses custom username validator
    Password string `json:"password" binding:"required,strongpassword"`     // Uses custom password validator  
    Email    string `json:"email" binding:"required,email"`                // Uses built-in email validator
    Phone    string `json:"phone" binding:"omitempty,phonenumber"`         // Optional phone with custom validation
}

// Advanced validation example with multiple conditions
type ProductRequest struct {
    Name        string  `json:"name" binding:"required,min=2,max=100"`
    Price       float64 `json:"price" binding:"required,gt=0"`              // Must be greater than 0
    Category    string  `json:"category" binding:"required,oneof=electronics clothing books"`
    SKU         string  `json:"sku" binding:"required,len=8,alphanum"`      // Exactly 8 alphanumeric characters
    Description string  `json:"description" binding:"max=500"`              // Optional, max 500 characters
}

```

**Custom Validator Benefits:**

1. **Business Logic**: Encode business rules directly in validation
2. **Reusability**: Use same validators across multiple structs
3. **Maintainability**: Centralized validation logic
4. **Consistency**: Ensure same rules applied everywhere

**When to Use Custom Validators:**

- Complex business rules (password strength, username format)
- Domain-specific validation (product codes, license plates)
- Cross-field validation (password confirmation)
- External validation (checking if email exists)

## Gin Testing Examples - Ensuring Code Quality

Testing is crucial for maintaining code quality and catching bugs early. Gin provides excellent testing support with built-in test mode and helpers.

### Testing Philosophy

1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test component interactions
3. **End-to-End Tests**: Test complete user workflows
4. **Test Coverage**: Aim for high coverage of critical paths

### Handler Testing - Testing Individual Endpoints

```go
package handlers_test

import (
    "bytes"
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "testing"
    
    "github.com/gin-gonic/gin"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/mock"
    
    "your-project/internal/handlers"
    "your-project/internal/models"
)

func TestUserHandler_CreateUser(t *testing.T) {
    // Set Gin to test mode
    gin.SetMode(gin.TestMode)
    
    // Create mock service
    mockService := new(MockUserService)
    handler := handlers.NewUserHandler(mockService)
    
    // Test data
    userReq := models.CreateUserRequest{
        Name:     "John Doe",
        Email:    "john@example.com",
        Password: "password123",
    }
    
    expectedUser := &models.User{
        ID:    1,
        Name:  "John Doe",
        Email: "john@example.com",
    }
    
    mockService.On("CreateUser", mock.AnythingOfType("*models.CreateUserRequest")).Return(expectedUser, nil)
    
    // Create request
    jsonData, _ := json.Marshal(userReq)
    req := httptest.NewRequest("POST", "/api/v1/users", bytes.NewBuffer(jsonData))
    req.Header.Set("Content-Type", "application/json")
    
    // Create response recorder
    w := httptest.NewRecorder()
    
    // Create Gin context
    c, _ := gin.CreateTestContext(w)
    c.Request = req
    
    // Call handler
    handler.CreateUser(c)
    
    // Assertions
    assert.Equal(t, http.StatusCreated, w.Code)
    
    var response handlers.GinResponse
    err := json.Unmarshal(w.Body.Bytes(), &response)
    assert.NoError(t, err)
    assert.True(t, response.Success)
    
    mockService.AssertExpectations(t)
}

func TestUserHandler_GetUsers_WithPagination(t *testing.T) {
    gin.SetMode(gin.TestMode)
    
    mockService := new(MockUserService)
    handler := handlers.NewUserHandler(mockService)
    
    users := []*models.User{
        {ID: 1, Name: "User 1", Email: "user1@example.com"},
        {ID: 2, Name: "User 2", Email: "user2@example.com"},
    }
    
    mockService.On("GetUsers", 1, 20, "", "").Return(users, 2, nil)
    
    req := httptest.NewRequest("GET", "/api/v1/users?page=1&limit=20", nil)
    w := httptest.NewRecorder()
    
    c, _ := gin.CreateTestContext(w)
    c.Request = req
    
    handler.GetUsers(c)
    
    assert.Equal(t, http.StatusOK, w.Code)
    mockService.AssertExpectations(t)
}

```

### Integration Testing with Gin

```go
package integration_test

import (
    "bytes"
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "testing"
    
    "github.com/gin-gonic/gin"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/suite"
    
    "your-project/internal/config"
    "your-project/cmd/api"
)

type APITestSuite struct {
    suite.Suite
    router *gin.Engine
    server *api.Server
}

func (suite *APITestSuite) SetupSuite() {
    gin.SetMode(gin.TestMode)
    
    cfg := &config.Config{
        Environment: "test",
        DatabaseURL: "postgres://test:test@localhost/test_db?sslmode=disable",
        JWTSecret:   "test-secret",
    }
    
    server, err := api.NewServer(cfg)
    suite.NoError(err)
    
    suite.server = server
    suite.router = server.Router()
}

func (suite *APITestSuite) TestCreateAndGetUser() {
    // Create user
    userReq := map[string]interface{}{
        "name":     "Test User",
        "email":    "test@example.com",
        "password": "password123",
    }
    
    jsonData, _ := json.Marshal(userReq)
    req := httptest.NewRequest("POST", "/api/v1/users", bytes.NewBuffer(jsonData))
    req.Header.Set("Content-Type", "application/json")
    
    w := httptest.NewRecorder()
    suite.router.ServeHTTP(w, req)
    
    suite.Equal(http.StatusCreated, w.Code)
    
    // Parse response to get user ID
    var createResponse struct {
        Data struct {
            ID int `json:"id"`
        } `json:"data"`
    }
    json.Unmarshal(w.Body.Bytes(), &createResponse)
    
    // Get user
    req = httptest.NewRequest("GET", fmt.Sprintf("/api/v1/users/%d", createResponse.Data.ID), nil)
    w = httptest.NewRecorder()
    suite.router.ServeHTTP(w, req)
    
    suite.Equal(http.StatusOK, w.Code)
}

func TestAPITestSuite(t *testing.T) {
    suite.Run(t, new(APITestSuite))
}

```

## Gin Performance Optimization

### Response Compression

```go
package middleware

import (
    "github.com/gin-contrib/gzip"
    "github.com/gin-gonic/gin"
)

func SetupCompression(r *gin.Engine) {
    // Add gzip compression
    r.Use(gzip.Gzip(gzip.DefaultCompression))
}

```

### Caching Middleware

```go
package middleware

import (
    "time"
    
    "github.com/gin-contrib/cache"
    "github.com/gin-contrib/cache/persistence"
    "github.com/gin-gonic/gin"
)

func SetupCache(r *gin.Engine) {
    // In-memory cache
    store := persistence.NewInMemoryStore(time.Second)
    
    // Cache specific endpoints
    r.GET("/api/v1/users", cache.CachePage(store, 5*time.Minute, handlers.GetUsers))
}

```

### Database Connection Pooling with Gin

```go
package database

import (
    "database/sql"
    "time"
    
    "github.com/gin-gonic/gin"
    _ "github.com/lib/pq"
)

func SetupDatabase(cfg *config.Config) (*sql.DB, error) {
    db, err := sql.Open("postgres", cfg.DatabaseURL)
    if err != nil {
        return nil, err
    }
    
    // Configure connection pool
    db.SetMaxOpenConns(25)
    db.SetMaxIdleConns(5)
    db.SetConnMaxLifetime(5 * time.Minute)
    db.SetConnMaxIdleTime(1 * time.Minute)
    
    return db, db.Ping()
}

// Database middleware to inject DB into context
func DatabaseMiddleware(db *sql.DB) gin.HandlerFunc {
    return func(c *gin.Context) {
        c.Set("db", db)
        c.Next()
    }
}

```

```go
package handlers

import (
    "encoding/json"
    "net/http"
    "strconv"
    
    "github.com/gorilla/mux"
    "your-project/internal/models"
    "your-project/internal/service"
)

type UserHandler struct {
    userService service.UserService
}

func NewUserHandler(userService service.UserService) *UserHandler {
    return &UserHandler{
        userService: userService,
    }
}

// GET /api/v1/users
func (h *UserHandler) GetUsers(w http.ResponseWriter, r *http.Request) {
    // Parse query parameters
    page, _ := strconv.Atoi(r.URL.Query().Get("page"))
    if page < 1 {
        page = 1
    }
    
    limit, _ := strconv.Atoi(r.URL.Query().Get("limit"))
    if limit < 1 || limit > 100 {
        limit = 20
    }
    
    users, total, err := h.userService.GetUsers(page, limit)
    if err != nil {
        models.WriteError(w, http.StatusInternalServerError, "INTERNAL_ERROR", 
            "Failed to retrieve users", nil)
        return
    }
    
    response := map[string]interface{}{
        "users": users,
        "pagination": map[string]interface{}{
            "page":  page,
            "limit": limit,
            "total": total,
        },
    }
    
    models.WriteJSON(w, http.StatusOK, response)
}

// POST /api/v1/users
func (h *UserHandler) CreateUser(w http.ResponseWriter, r *http.Request) {
    var user models.User
    
    if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
        models.WriteError(w, http.StatusBadRequest, "INVALID_JSON", 
            "Invalid JSON format", nil)
        return
    }
    
    // Validate user data
    if err := user.Validate(); err != nil {
        models.WriteError(w, http.StatusBadRequest, "VALIDATION_ERROR", 
            "Invalid user data", err)
        return
    }
    
    createdUser, err := h.userService.CreateUser(&user)
    if err != nil {
        if err == service.ErrUserExists {
            models.WriteError(w, http.StatusConflict, "USER_EXISTS", 
                "User already exists", nil)
            return
        }
        models.WriteError(w, http.StatusInternalServerError, "INTERNAL_ERROR", 
            "Failed to create user", nil)
        return
    }
    
    models.WriteJSON(w, http.StatusCreated, createdUser)
}

// GET /api/v1/users/{id}
func (h *UserHandler) GetUser(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    id, err := strconv.Atoi(vars["id"])
    if err != nil {
        models.WriteError(w, http.StatusBadRequest, "INVALID_ID", 
            "Invalid user ID", nil)
        return
    }
    
    user, err := h.userService.GetUser(id)
    if err != nil {
        if err == service.ErrUserNotFound {
            models.WriteError(w, http.StatusNotFound, "USER_NOT_FOUND", 
                "User not found", nil)
            return
        }
        models.WriteError(w, http.StatusInternalServerError, "INTERNAL_ERROR", 
            "Failed to retrieve user", nil)
        return
    }
    
    models.WriteJSON(w, http.StatusOK, user)
}

```

## Data Models & Validation

### User Model with Validation

```go
package models

import (
    "errors"
    "regexp"
    "time"
)

type User struct {
    ID        int       `json:"id" db:"id"`
    Name      string    `json:"name" db:"name"`
    Email     string    `json:"email" db:"email"`
    Password  string    `json:"password,omitempty" db:"password"`
    CreatedAt time.Time `json:"created_at" db:"created_at"`
    UpdatedAt time.Time `json:"updated_at" db:"updated_at"`
}

type CreateUserRequest struct {
    Name     string `json:"name" validate:"required,min=2,max=50"`
    Email    string `json:"email" validate:"required,email"`
    Password string `json:"password" validate:"required,min=8"`
}

type UpdateUserRequest struct {
    Name  string `json:"name,omitempty" validate:"omitempty,min=2,max=50"`
    Email string `json:"email,omitempty" validate:"omitempty,email"`
}

var emailRegex = regexp.MustCompile(`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`)

func (u *User) Validate() error {
    var errs []string
    
    if u.Name == "" {
        errs = append(errs, "name is required")
    } else if len(u.Name) < 2 || len(u.Name) > 50 {
        errs = append(errs, "name must be between 2 and 50 characters")
    }
    
    if u.Email == "" {
        errs = append(errs, "email is required")
    } else if !emailRegex.MatchString(u.Email) {
        errs = append(errs, "invalid email format")
    }
    
    if len(errs) > 0 {
        return errors.New("validation failed: " + errs[0])
    }
    
    return nil
}

// Using go-playground/validator
package models

import (
    "github.com/go-playground/validator/v10"
)

var validate *validator.Validate

func init() {
    validate = validator.New()
}

func (req *CreateUserRequest) Validate() error {
    return validate.Struct(req)
}

func (req *UpdateUserRequest) Validate() error {
    return validate.Struct(req)
}

```

## Database Integration

### Database Interface

```go
package repository

import "your-project/internal/models"

type UserRepository interface {
    Create(user *models.User) (*models.User, error)
    GetByID(id int) (*models.User, error)
    GetByEmail(email string) (*models.User, error)
    Update(id int, user *models.User) (*models.User, error)
    Delete(id int) error
    List(offset, limit int) ([]*models.User, int, error)
}

```

### PostgreSQL Implementation

```go
package repository

import (
    "database/sql"
    "time"
    
    "your-project/internal/models"
    _ "github.com/lib/pq"
)

type postgresUserRepo struct {
    db *sql.DB
}

func NewPostgresUserRepo(db *sql.DB) UserRepository {
    return &postgresUserRepo{db: db}
}

func (r *postgresUserRepo) Create(user *models.User) (*models.User, error) {
    query := `
        INSERT INTO users (name, email, password, created_at, updated_at)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING id`
    
    now := time.Now()
    err := r.db.QueryRow(query, user.Name, user.Email, user.Password, now, now).Scan(&user.ID)
    if err != nil {
        return nil, err
    }
    
    user.CreatedAt = now
    user.UpdatedAt = now
    user.Password = "" // Don't return password
    
    return user, nil
}

func (r *postgresUserRepo) GetByID(id int) (*models.User, error) {
    user := &models.User{}
    query := `
        SELECT id, name, email, created_at, updated_at
        FROM users WHERE id = $1`
    
    err := r.db.QueryRow(query, id).Scan(
        &user.ID, &user.Name, &user.Email, 
        &user.CreatedAt, &user.UpdatedAt)
    
    if err == sql.ErrNoRows {
        return nil, ErrUserNotFound
    }
    
    return user, err
}

func (r *postgresUserRepo) List(offset, limit int) ([]*models.User, int, error) {
    // Get total count
    var total int
    countQuery := "SELECT COUNT(*) FROM users"
    err := r.db.QueryRow(countQuery).Scan(&total)
    if err != nil {
        return nil, 0, err
    }
    
    // Get users
    query := `
        SELECT id, name, email, created_at, updated_at
        FROM users
        ORDER BY created_at DESC
        LIMIT $1 OFFSET $2`
    
    rows, err := r.db.Query(query, limit, offset)
    if err != nil {
        return nil, 0, err
    }
    defer rows.Close()
    
    var users []*models.User
    for rows.Next() {
        user := &models.User{}
        err := rows.Scan(&user.ID, &user.Name, &user.Email, 
            &user.CreatedAt, &user.UpdatedAt)
        if err != nil {
            return nil, 0, err
        }
        users = append(users, user)
    }
    
    return users, total, nil
}

```

## Error Handling

### Custom Errors

```go
package service

import "errors"

var (
    ErrUserNotFound    = errors.New("user not found")
    ErrUserExists      = errors.New("user already exists")
    ErrInvalidPassword = errors.New("invalid password")
    ErrUnauthorized    = errors.New("unauthorized")
)

type ValidationError struct {
    Field   string `json:"field"`
    Message string `json:"message"`
}

type ValidationErrors []ValidationError

func (ve ValidationErrors) Error() string {
    return "validation failed"
}

```

### Error Handler Middleware

```go
package middleware

import (
    "encoding/json"
    "net/http"
    "your-project/internal/models"
)

func ErrorHandler(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                models.WriteError(w, http.StatusInternalServerError, 
                    "INTERNAL_ERROR", "Internal server error", nil)
            }
        }()
        
        next.ServeHTTP(w, r)
    })
}

```

## Authentication & Authorization

### JWT Implementation

```go
package auth

import (
    "time"
    
    "github.com/golang-jwt/jwt/v4"
)

type Claims struct {
    UserID string `json:"user_id"`
    Email  string `json:"email"`
    jwt.RegisteredClaims
}

func GenerateToken(userID, email string, secret []byte) (string, error) {
    claims := &Claims{
        UserID: userID,
        Email:  email,
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(time.Now().Add(24 * time.Hour)),
            IssuedAt:  jwt.NewNumericDate(time.Now()),
            Issuer:    "your-api",
        },
    }
    
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(secret)
}

func ValidateToken(tokenString string, secret []byte) (*Claims, error) {
    claims := &Claims{}
    
    token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
        return secret, nil
    })
    
    if err != nil {
        return nil, err
    }
    
    if !token.Valid {
        return nil, jwt.ErrSignatureInvalid
    }
    
    return claims, nil
}

```

### Login Handler

```go
package handlers

import (
    "encoding/json"
    "net/http"
    
    "golang.org/x/crypto/bcrypt"
    "your-project/internal/auth"
    "your-project/internal/models"
)

type AuthHandler struct {
    userService service.UserService
    jwtSecret   []byte
}

type LoginRequest struct {
    Email    string `json:"email" validate:"required,email"`
    Password string `json:"password" validate:"required"`
}

type LoginResponse struct {
    Token string       `json:"token"`
    User  *models.User `json:"user"`
}

func (h *AuthHandler) Login(w http.ResponseWriter, r *http.Request) {
    var req LoginRequest
    
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        models.WriteError(w, http.StatusBadRequest, "INVALID_JSON", 
            "Invalid JSON format", nil)
        return
    }
    
    user, err := h.userService.GetUserByEmail(req.Email)
    if err != nil {
        models.WriteError(w, http.StatusUnauthorized, "INVALID_CREDENTIALS", 
            "Invalid email or password", nil)
        return
    }
    
    if err := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(req.Password)); err != nil {
        models.WriteError(w, http.StatusUnauthorized, "INVALID_CREDENTIALS", 
            "Invalid email or password", nil)
        return
    }
    
    token, err := auth.GenerateToken(strconv.Itoa(user.ID), user.Email, h.jwtSecret)
    if err != nil {
        models.WriteError(w, http.StatusInternalServerError, "TOKEN_ERROR", 
            "Failed to generate token", nil)
        return
    }
    
    user.Password = "" // Don't return password
    
    response := LoginResponse{
        Token: token,
        User:  user,
    }
    
    models.WriteJSON(w, http.StatusOK, response)
}

```

## Testing

### Unit Test Example

```go
package handlers_test

import (
    "bytes"
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "testing"
    
    "github.com/gorilla/mux"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/mock"
    
    "your-project/internal/handlers"
    "your-project/internal/models"
)

type MockUserService struct {
    mock.Mock
}

func (m *MockUserService) CreateUser(user *models.User) (*models.User, error) {
    args := m.Called(user)
    return args.Get(0).(*models.User), args.Error(1)
}

func TestCreateUser(t *testing.T) {
    mockService := new(MockUserService)
    handler := handlers.NewUserHandler(mockService)
    
    user := &models.User{
        Name:  "John Doe",
        Email: "john@example.com",
    }
    
    expectedUser := &models.User{
        ID:    1,
        Name:  "John Doe",
        Email: "john@example.com",
    }
    
    mockService.On("CreateUser", mock.AnythingOfType("*models.User")).Return(expectedUser, nil)
    
    jsonUser, _ := json.Marshal(user)
    req := httptest.NewRequest("POST", "/api/v1/users", bytes.NewBuffer(jsonUser))
    req.Header.Set("Content-Type", "application/json")
    
    rr := httptest.NewRecorder()
    handler.CreateUser(rr, req)
    
    assert.Equal(t, http.StatusCreated, rr.Code)
    
    var response models.APIResponse
    json.Unmarshal(rr.Body.Bytes(), &response)
    assert.True(t, response.Success)
    
    mockService.AssertExpectations(t)
}

```

### Integration Test Example

```go
package main_test

import (
    "bytes"
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "testing"
    
    "github.com/stretchr/testify/assert"
    "your-project/cmd/api"
)

func TestUserAPI(t *testing.T) {
    // Setup test database and server
    server := api.SetupTestServer()
    
    t.Run("Create User", func(t *testing.T) {
        user := map[string]string{
            "name":     "Test User",
            "email":    "test@example.com",
            "password": "password123",
        }
        
        jsonUser, _ := json.Marshal(user)
        req := httptest.NewRequest("POST", "/api/v1/users", bytes.NewBuffer(jsonUser))
        req.Header.Set("Content-Type", "application/json")
        
        rr := httptest.NewRecorder()
        server.ServeHTTP(rr, req)
        
        assert.Equal(t, http.StatusCreated, rr.Code)
    })
    
    t.Run("Get Users", func(t *testing.T) {
        req := httptest.NewRequest("GET", "/api/v1/users", nil)
        rr := httptest.NewRecorder()
        
        server.ServeHTTP(rr, req)
        
        assert.Equal(t, http.StatusOK, rr.Code)
    })
}

```

## Documentation

### OpenAPI/Swagger Specification

```yaml
openapi: 3.0.0
info:
  title: User API
  description: REST API for user management
  version: 1.0.0
  contact:
    name: API Support
    email: support@example.com

servers:
  - url: http://localhost:8080/api/v1
    description: Development server

paths:
  /users:
    get:
      summary: Get all users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            minimum: 1
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
      responses:
        '200':
          description: List of users
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      users:
                        type: array
                        items:
                          $ref: '#/components/schemas/User'
                      pagination:
                        $ref: '#/components/schemas/Pagination'
                  success:
                    type: boolean
                  meta:
                    $ref: '#/components/schemas/Meta'
    
    post:
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/User'
                  success:
                    type: boolean
                  meta:
                    $ref: '#/components/schemas/Meta'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    
    CreateUserRequest:
      type: object
      required:
        - name
        - email
        - password
      properties:
        name:
          type: string
          minLength: 2
          maxLength: 50
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 8

```

### Generating Documentation

```go
// Using swaggo/swag for generating docs from comments

//go:generate swag init -g cmd/api/main.go -o ./docs

// @title User API
// @version 1.0
// @description REST API for user management
// @host localhost:8080
// @BasePath /api/v1

// @securityDefinitions.apikey BearerAuth
// @in header
// @name Authorization

// GetUsers godoc
// @Summary Get all users
// @Description Get a list of all users with pagination
// @Tags users
// @Accept json
// @Produce json
// @Param page query int false "Page number" default(1)
// @Param limit query int false "Items per page" default(20)
// @Success 200 {object} models.APIResponse{data=map[string]interface{}}
// @Failure 500 {object} models.APIResponse
// @Router /users [get]
func (h *UserHandler) GetUsers(w http.ResponseWriter, r *http.Request) {
    // Implementation
}

```

## Performance & Monitoring

### Database Connection Pooling

```go
package database

import (
    "database/sql"
    "time"
    
    _ "github.com/lib/pq"
)

func NewConnection(databaseURL string) (*sql.DB, error) {
    db, err := sql.Open("postgres", databaseURL)
    if err != nil {
        return nil, err
    }
    
    // Configure connection pool
    db.SetMaxOpenConns(25)                 // Maximum open connections
    db.SetMaxIdleConns(5)                  // Maximum idle connections
    db.SetConnMaxLifetime(5 * time.Minute) // Connection max lifetime
    db.SetConnMaxIdleTime(1 * time.Minute) // Connection max idle time
    
    if err := db.Ping(); err != nil {
        return nil, err
    }
    
    return db, nil
}

```

### Metrics Collection

```go
package middleware

import (
    "net/http"
    "strconv"
    "time"
    
    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promauto"
)

var (
    httpDuration = promauto.NewHistogramVec(prometheus.HistogramOpts{
        Name: "http_duration_seconds",
        Help: "Duration of HTTP requests.",
    }, []string{"method", "path", "status_code"})
    
    httpRequests = promauto.NewCounterVec(prometheus.CounterOpts{
        Name: "http_requests_total",
        Help: "Total number of HTTP requests.",
    }, []string{"method", "path", "status_code"})
)

func MetricsMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        
        wrapper := &responseWriter{ResponseWriter: w, statusCode: http.StatusOK}
        next.ServeHTTP(wrapper, r)
        
        duration := time.Since(start).Seconds()
        statusCode := strconv.Itoa(wrapper.statusCode)
        
        httpDuration.WithLabelValues(r.Method, r.URL.Path, statusCode).Observe(duration)
        httpRequests.WithLabelValues(r.Method, r.URL.Path, statusCode).Inc()
    })
}

```

### Health Check Endpoint

```go
package handlers

import (
    "database/sql"
    "encoding/json"
    "net/http"
    "time"
)

type HealthHandler struct {
    db *sql.DB
}

type HealthResponse struct {
    Status   string            `json:"status"`
    Checks   map[string]string `json:"checks"`
    Version  string            `json:"version"`
    Uptime   string            `json:"uptime"`
}

var startTime = time.Now()

func (h *HealthHandler) Health(w http.ResponseWriter, r *http.Request) {
    checks := make(map[string]string)
    status := "healthy"
    
    // Database check
    if err := h.db.Ping(); err != nil {
        checks["database"] = "unhealthy"
        status = "unhealthy"
    } else {
        checks["database"] = "healthy"
    }
    
    response := HealthResponse{
        Status:  status,
        Checks:  checks,
        Version: "1.0.0",
        Uptime:  time.Since(startTime).String(),
    }
    
    statusCode := http.StatusOK
    if status == "unhealthy" {
        statusCode = http.StatusServiceUnavailable
    }
    
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(statusCode)
    json.NewEncoder(w).Encode(response)
}

```

## Configuration Management

### Environment Configuration

```go
package config

import (
    "os"
    "strconv"
)

type Config struct {
    Port        string
    DatabaseURL string
    JWTSecret   string
    LogLevel    string
    Environment string
}

func Load() *Config {
    return &Config{
        Port:        getEnv("PORT", "8080"),
        DatabaseURL: getEnv("DATABASE_URL", "postgres://localhost/mydb?sslmode=disable"),
        JWTSecret:   getEnv("JWT_SECRET", "your-secret-key"),
        LogLevel:    getEnv("LOG_LEVEL", "info"),
        Environment: getEnv("ENVIRONMENT", "development"),
    }
}

func getEnv(key, fallback string) string {
    if value := os.Getenv(key); value != "" {
        return value
    }
    return fallback
}

func getEnvAsInt(key string, fallback int) int {
    if value := os.Getenv(key); value != "" {
        if intVal, err := strconv.Atoi(value); err == nil {
            return intVal
        }
    }
    return fallback
}

```

## Deployment

### Dockerfile

```dockerfile
# Build stage
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main cmd/api/main.go

# Final stage
FROM alpine:latest

RUN apk --no-cache add ca-certificates
WORKDIR /root/

# Copy the binary from builder stage
COPY --from=builder /app/main .

# Expose port
EXPOSE 8080

# Run the application
CMD ["./main"]

```

### Docker Compose

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgres://user:password@db:5432/mydb?sslmode=disable
      - JWT_SECRET=your-jwt-secret
      - ENVIRONMENT=production
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:

```

## Key Takeaways - Building Production-Ready APIs with Gin

### Architecture Principles

1. **Layered Architecture**: Separate concerns into distinct layers
   - **Handlers**: HTTP request/response processing
   - **Services**: Business logic and validation
   - **Repositories**: Data access and persistence
   - **Models**: Data structures and validation rules

2. **Dependency Injection**: Inject dependencies at startup
   - Makes testing easier with mock dependencies
   - Promotes loose coupling between components
   - Clear dependency management and initialization

3. **Middleware-First Approach**: Use middleware for cross-cutting concerns
   - Authentication and authorization
   - Logging and monitoring
   - Rate limiting and security
   - Error handling and recovery

### Performance and Scalability

1. **Connection Pooling**: Properly configure database connections
   - Set appropriate pool sizes for your workload
   - Monitor connection usage and adjust as needed
   - Use connection timeouts to prevent resource leaks

2. **Caching Strategy**: Implement caching at multiple levels
   - HTTP response caching for frequently accessed data
   - Database query result caching
   - Application-level caching for expensive operations

3. **Rate Limiting**: Protect your API from abuse
   - Implement both global and per-user rate limits
   - Use appropriate algorithms (token bucket, sliding window)
   - Provide clear error messages when limits are exceeded

### Security Best Practices

1. **Authentication**: Implement robust user authentication
   - Use JWT tokens with appropriate expiration times
   - Implement refresh token mechanism
   - Store secrets securely and rotate them regularly

2. **Input Validation**: Validate all incoming data
   - Use Gin's built-in validation features
   - Implement custom validators for business rules
   - Sanitize input to prevent injection attacks

3. **Security Headers**: Add appropriate HTTP security headers
   - CORS for cross-origin requests
   - Security headers to prevent common attacks
   - HTTPS enforcement in production

### Monitoring and Observability

1. **Logging**: Implement comprehensive logging
   - Structure logs for easy parsing
   - Include request IDs for tracing
   - Log at appropriate levels (debug, info, warn, error)

2. **Metrics**: Collect essential metrics
   - Request rate and response times
   - Error rates and types
   - Resource usage (CPU, memory, database connections)

3. **Health Checks**: Implement health check endpoints
   - Check database connectivity
   - Verify external service availability
   - Provide detailed status information

### Testing Strategy

1. **Unit Tests**: Test individual components
   - Use mocks to isolate dependencies
   - Test both success and error scenarios
   - Aim for high code coverage

2. **Integration Tests**: Test component interactions
   - Use test databases or containers
   - Test complete workflows
   - Verify data persistence and retrieval

3. **End-to-End Tests**: Test from user perspective
   - Test complete user journeys
   - Use realistic test data
   - Automate critical path testing

### Deployment Considerations

1. **Environment Configuration**: Use environment-based configuration
   - Separate configuration for development, staging, production
   - Secure handling of secrets and credentials
   - Easy configuration updates without code changes

2. **Containerization**: Use Docker for consistent deployments
   - Multi-stage builds for optimized images
   - Proper handling of signals and graceful shutdown
   - Health checks for container orchestration

3. **Scalability**: Design for horizontal scaling
   - Stateless application design
   - Database connection pooling
   - Load balancer compatibility

### Gin-Specific Best Practices

1. **Middleware Organization**: Structure middleware logically
   - Apply global middleware for all routes
   - Use route groups for specific middleware
   - Order middleware appropriately

2. **Error Handling**: Implement consistent error responses
   - Use standardized error response format
   - Provide helpful error messages
   - Log errors appropriately for debugging

3. **Validation**: Leverage Gin's validation features
   - Use struct tags for automatic validation
   - Implement custom validators for business rules
   - Provide clear validation error messages

4. **Testing**: Take advantage of Gin's testing support
   - Use test mode to disable debug output
   - Create test contexts for handler testing
   - Test middleware and route configurations

Remember: Building a production-ready API is about more than just writing code. It requires careful consideration of architecture, security, performance, monitoring, and maintainability. Gin provides excellent tools to implement these best practices efficiently.


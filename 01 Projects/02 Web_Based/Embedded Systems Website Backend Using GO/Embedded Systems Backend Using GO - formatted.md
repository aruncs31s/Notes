---
tags:
  - "#backend"
  - "#go"
  - "#website"
  - "#project"
---

# Embedded Systems Backend Using Go

## Project Structure

The project follows a clean architecture pattern with separated concerns:

- **handlers/**: Contains HTTP request handlers
- **initializers/**: Database and environment initialization
- **routes/**: API route definitions

```text
├── es_website_gcek_backend
├── go.mod
├── go.sum
├── handlers
│   ├── getName.go
│   ├── register.go
│   └── test.go
├── initializers
│   ├── initDB.go
│   └── loadEnvVars.go
├── main.go
└── routes
    ├── routes.go
    └── test.go

4 directories, 11 files
```


## Database Logo ? 
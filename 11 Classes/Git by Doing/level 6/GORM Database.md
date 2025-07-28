
# GORM Database 

When adding `GetByUsername`
? Should i always 

**Repository pattern interface**
? To abstract the data access layer of an Application
```go
 type StudentsRepository interface {
        GetAll() ([]models.Students, error)
        Update(student *models.Students) error
        Delete(id uint) error
 }

```

## Adding New Method.
1. Add `GetByUsername` to the Repository Interface
2. Implement `GetByUsername` in the Student Repository
3. Use the New Method in Your Handler
# 4. Update `database.go` to Use the Handler Correctly
### Updatin the interface 

```go 
type StudentsRepository interface {
        GetAll() ([]models.Students, error)
        Update(student *models.Students) error
        Delete(id uint) error
      	GetByUsername(username string) (*models.Students, error)
 }
```
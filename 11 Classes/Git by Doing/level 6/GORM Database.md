
# GORM Database 

When adding `GetByUsername`
? Should i al
```go
 type StudentsRepository interface {
        GetAll() ([]models.Students, error)
        Update(student *models.Students) error
        Delete(id uint) error
      	GetByUsername(username string) (*models.Students, error)
 }

```
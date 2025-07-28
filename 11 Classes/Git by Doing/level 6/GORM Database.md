
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


### Updatin the interface 

```go 
type StudentsRepository interface {
        GetAll() ([]models.Students, error)
        Update(student *models.Students) error
        Delete(id uint) error
      	GetByUsername(username string) (*models.Students, error)
 }
```
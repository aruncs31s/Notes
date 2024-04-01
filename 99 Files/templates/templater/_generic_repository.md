<%*

let tableName = await tp.system.prompt("Enter the table name (e.g., staff_project_guided):");

// Convert snake_case to PascalCase for struct names
let structName = tableName
    .split('_')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join('');

// Generate repository-specific names
let repoStructName = structName + "Repository";
let readerInterfaceName = structName + "Reader";
let writerInterfaceName = structName + "Writer";
let privateRepoName = tableName + "Repository";

// Store for later use
%>

# Repository: <% structName %>

## Type Contract

```go
type <% structName %> interface {
	<% readerInterfaceName %>
	<% writerInterfaceName %>
}
```

#### Members 
```go
type <% privateRepoName %> struct {
	reader <% readerInterfaceName %>
	writer <% writerInterfaceName %>
}
```

### Reader
```go
type <% readerInterfaceName %> interface {
	FindByStaffID(staffID int, limit int, offset int) (*[]<% structName %>, error)
	CountByStaffID(staffID int) (int64, error)
	FindByID(id int) (*<% structName %>, error)
}
```

### Writer
```go
type <% writerInterfaceName %> interface {
	Create(project *model.<% structName %>) (*model.<% structName %>, error)
	Update(project *model.<% structName %>) (*model.<% structName %>, error)
	Delete(project *model.<% structName %>) error
}
```

## Constructors 

```go
func New<% structName %>Repository(db *gorm.DB) *<% privateRepoName %> {
	reader := New<% structName %>RepositoryReader(db)
	writer := New<% structName %>RepositoryWriter(db)
	return &<% privateRepoName %>{
		reader: reader,
		writer: writer,
	}
}
```

## Methods

```go

func (r *<% privateRepoName %>) FindByStaffID(staffID int, limit int, offset int) (*[]<% structName %>, error) {
	// Implementation goes here
	return nil, nil
}

func (r *<% privateRepoName %>) CountByStaffID(staffID int) (int64, error) {
	// Implementation goes here
	return 0, nil
}

func (r *<% privateRepoName %>) FindByID(id int) (*<% structName %>, error) {
	// Implementation goes here
	return nil, nil
}

func (r *<% privateRepoName %>) Create(project *model.<% structName %>) (*model.<% structName %>, error) {
	// Implementation goes here
	return nil, nil
}

func (r *<% privateRepoName %>) Update(project *model.<% structName %>) (*model.<% structName %>, error) {
	// Implementation goes here
	return nil, nil
}

func (r *<% privateRepoName %>) Delete(project *model.<% structName %>) error {
	// Implementation goes here
	return nil
}

```
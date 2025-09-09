---
id: Parsing_JSON
aliases: []
tags:
  - classes
  - git_by_doing
dg-publish: true
---
# without Channels

```go
func ReadStudentsFromJSON() ([]Student, error) {
	data, err := os.ReadFile("students/students_details.json")
	if err != nil {
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	// Parse as map[string]string (username -> name)
	var studentMap map[string]string
	err = json.Unmarshal(data, &studentMap)
	if err != nil {
		return nil, fmt.Errorf("error parsing JSON: %v", err)
	}

	// Convert to []Student slice
	var students []Student
	for username, name := range studentMap {
		students = append(students, Student{
			Name:     name,
			Username: username,
		})
	}

	return students, nil
}

func DisplayStudents(students []Student) {
	fmt.Println("📚 Student Details:")

	for _, student := range students {
		fmt.Printf("   Name: %s\n", student.Name)
		fmt.Printf("   username: %s\n", student.Username)
	}
}

```

# With channels
- [ ]  Paste here from code 🏁 delete 

```go

```
# Project Creation

Data i take from the Web Front end.X
```ts
export interface ProjectCreateData {
  title: string;
  description: string;
  status: ProjectStatusType;
  category: string;
  github_link?: string;
  live_url?: string;
  image?: string;
  technologies?: string[];
  contributors?: string[];
}
```

```go
type ProjectCreation struct {
	Title        string    `json:"title" example:"My Project"`
	Image        *string   `json:"image" example:"https://example.com/image.jpg"`
	Description  string    `json:"description" example:"This is a sample project description"`
	Status       string    `json:"status" example:"in_progress"`
	Visibility   string    `json:"visibility" example:"everyone"`
	GithubLink   string    `json:"github_link" example:"https://github.com/user/project"`
	Technologies *[]string `json:"technologies" example:"Go, Gin, GORM"`
	LiveURL      *string   `json:"live_url" example:"https://example.com/live"`
	Category     string    `json:"category" example:"Web Development"`
	Contributors *[]string `json:"contributors" example:"2,3,4"`
}
```

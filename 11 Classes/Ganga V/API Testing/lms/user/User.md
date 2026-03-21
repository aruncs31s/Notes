# User Module
- [ ] Create a User
- [ ] Get All Users
- [ ] Update a User
- [ ] Delete a User
---
## Get All User

- API Contract?? 

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQzNjQ5MDksInJvbGUiOiJ0ZWFjaGVyIiwidXNlcl9pZCI6ImIyOWQxMjcxLWVlNDQtNDNmNS1hZmFhLWViNjk1ZTkxZmUxZiJ9.KlpBGemBlfXBRECiIBlw5ySK2tYZmzZgYhv1tcRae-c",
    "user": {
        "id": "b29d1271-ee44-43f5-afaa-eb695e91fe1f",
        "first_name": "Ganga",
        "last_name": "V",
        "email": "ganga@gamil.com",
        "role": "teacher"
    }
}
```


```go 
type loginResponse struct{
	Token string
	User any
	Roles []string
}
```

```python
class LoginResponse:
	Token: str
	User: any
```
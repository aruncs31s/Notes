## Register


```bash
curl -X POST http://localhost:8080/api/v1/user/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Arun CS",
    "email": "aruncs31ss@gmail.com",
    "username": "aruncs31s",
    "password": "password123"
  }'
```

```jwt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjQ3MDgwNTAsImlhdCI6MTc2NDQ5MjA1MCwiaXNzIjoiZXNkYy1iYWNrZW5kIiwicm9sZSI6InVzZXIiLCJzdWIiOiJhcnVuY3MzMXNzQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiYXJ1bmNzMzFzIn0.kAf2O-n-MskwrPaklmP1EEhZ3ValnSOZ_CEIvhXCsgk
```
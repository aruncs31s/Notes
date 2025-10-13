---
dg-publish: true
cssclasses:
  - wide-page
---

## `/api/admin/users`

URL : `{{ESDC_BACKEND_URL}}/api/admin/users`


```js
// Get All Users
GET /api/admin/users
Response: [{
  id: number,
  username: string,
  email: string,
  role: 'admin' | 'user',
  status: 'active' | 'inactive'
}]
```



```json
{
    "data": [
        {
            "id": 1,
            "name": "Arun CS",
            "username": "aruncs31s",
            "email": "aruncs31ss@gmail.com",
            "password": "12345678",
            "role": "admin",
            "verified": false,
            "status": "active",
            "created_at": 1759947806,
            "updated_at": 1759947806,
            "Github": null,
            "Submissions": null,
            "Details": null
        },
        {
            "id": 2,
            "name": "Test User",
            "username": "",
            "email": "test@gmail.com",
            "password": "12345678",
            "role": "user",
            "verified": false,
            "status": "active",
            "created_at": 1759951473,
            "updated_at": 1759951473,
            "Github": null,
            "Submissions": null,
            "Details": null
        },
    "meta": "2025-10-09T21:31:17+05:30",
    "status": true
}
```

## `/api/admin/stats`

```js
// Admin Stats
GET /api/admin/stats
Response: {
  totalUsers: number,
  totalProjects: number,
  totalChallenges: number,
  activeUsers: number
}
```


```json
{
    "data": {
        "total_users": 3,
        "total_projects": 0,
        "total_challenges": 5,
        "active_users": 2
    },
    "meta": "2025-10-09T21:37:25+05:30",
    "status": true
}
```


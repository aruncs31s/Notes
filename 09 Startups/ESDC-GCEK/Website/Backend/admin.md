---
id: admin
aliases: []
tags: []
---
# Admin

## Tasks

> Admin

- [ ] Get `/api/admin/stats` - Retrieve system statistics.
- [ ] Get `/api/admin/users` - List all users.
- [ ] Delete `/api/admin/users/:id` - Remove a user by ID.
- [ ] Put `/api/admin/users/:id` - Update user information by ID.

> Projects

- [ ] Get `/api/admin/projects` - List all projects.
- [ ] Post `/api/admin/projects` - Create a new project.
- [ ] Delete `/api/admin/projects/:id` - Remove a project by ID.
- [ ] Put `/api/admin/projects/:id` - Update project information by ID.

> Challenges

- [ ] Get `/api/admin/challenges` - List all challenges.
- [ ] Post `/api/admin/challenges` - Create a new challenge.
- [ ] Delete `/api/admin/challenges/:id` - Remove a challenge by ID.
- [ ] Put `/api/admin/challenges/:id` - Update challenge information by ID.

```bash
GET    /api/admin/stats
GET    /api/admin/users
DELETE /api/admin/users/:id
PUT    /api/admin/users/:id

GET    /api/admin/projects
POST   /api/admin/projects
DELETE /api/admin/projects/:id
PUT    /api/admin/projects/:id

GET    /api/admin/challenges
POST   /api/admin/challenges
DELETE /api/admin/challenges/:id
PUT    /api/admin/challenges/:id
```

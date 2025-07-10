---
tags:
  - es_website
  - backend
---

# Flask Backend 
>[!blank|right]
>- [[02 Flask APIs]]

The flask backend should do the followings
- [x] Manage authentication ✅ 2025-07-10


## Tokens

API tokens (like JWT - JSON Web Tokens) are generally preferred.
```js
const response = await fetch('/api/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email: 'user@example.com', password: 'password123' }),
});
const data = await response.json();
if (data.status === 'success') {
    localStorage.setItem('accessToken', data.access_token);
    // Redirect or update UI
} else {
console.log("HI")
    // Show error
}
```

## README.md -> frontmatter-rich

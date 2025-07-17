---
tags:
  - es_website
  - backend
---

# Flask Backend 
- [[YAML Conversion]]

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

**Subsequent API Calls(eg: upload)**
```js
const accessToken = localStorage.getItem('accessToken');
if (!accessToken) {
    // Handle not logged in
    return;
}

const formData = new FormData();
formData.append('profile_pic', yourFileObject); // For profile pic
// Or for readme: formData.append('readme_file', yourFileObject);

const response = await fetch('/api/upload_profile_pic', { // or /api/upload_readme
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${accessToken}`, // Crucial for token auth
    },
    body: formData,
});
const data = await response.json();
// Handle response
```

Install PyJWT:

Bash

pip install PyJWT
Generate a Secret Key for JWTs: This should be different from your app.secret_key. Store it securely (e.g., in environment variables).

Modify login to issue a JWT:
When a user successfully logs in, instead of setting a session variable, you'll generate a JWT and send it back to the client.

Create a decorator for token verification:
This decorator will protect your API routes, ensuring that a valid token is present in the request header.

Client-side handling:
Your Astro frontend will need to store this token (e.g., in localStorage) and include it in the Authorization header for subsequent API requests.
## README.md -> frontmatter-rich


## Login 

Src/stores/auth. Ts  rm this 


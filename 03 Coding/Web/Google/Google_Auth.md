---
id: Google_Auth
aliases: []
tags:
  - coding
  - web
  - google
dg-publish: true
---
## Steps

1. Goto https://console.developers.google.com
2. Create a new project
3. Go to API & Services > OAuth Consent Screen

- User Type: External
- App Name: Your App Name
- User Support Email: Your Email
- Developer Contact Information: Your Email

4. Save and Continue
5. Go to API & Services > Credentials
6. Add test users

- Add your email address

7. Create Credentials > OAuth Client ID
8. Application Type: Web application
9. Name: Your App Name
10. Authorized redirect URIs:

- http://localhost:3000/api/auth/callback/google

11. Save
12. Copy the Client ID and Client Secret
13. Go to your Next.js app
14. Create a `.env.local` file in the root of your project
15. Add the following environment variables:

```env
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
NEXTAUTH_URL=http://localhost:3000

```

16. Install the required packages:

```bash
npm install next-auth @next-auth/google

```

---
dg-publish: true
---

## Steps
>[!important|right]
>- [[es_gece_website_backend.code]]

1. Backend Initialization:  installed the Express.js framework to create web server.
```bash
npm init -y 
npm install express
```
- installed `passport` and `passport-google-oauth20`  to handle the Google OAuth flow. 
```bash
npm install passport passport-google-oauth20
```

2. Google OAuth Integration :  then added the basic Passport configuration, including a route to initiate Google Sign-In (`/auth/google`) and a callback route (`/auth/google/callback`).
```js
const passport = require('passport');
 const GoogleStrategy = require('passport-google-oauth20').Strategy;
 passport.use(new GoogleStrategy({
     clientID: GOOGLE_CLIENT_ID,
     clientSecret: GOOGLE_CLIENT_SECRET,
     callbackURL: "http://localhost:3000/auth/google/callback"
   },
   function(accessToken, refreshToken, profile, cb) {
     return cb(null, profile);
   }
 ));
 app.use(passport.initialize());
 
 app.get('/auth/google',
   passport.authenticate('google', { scope: ['profile', 'email'] }));
 
 app.get('/auth/google/callback',
   passport.authenticate('google', { failureRedirect: '/' }),
   function(req, res) {
     // Successful authentication, redirect home.
     res.redirect('/profile');
   });
```
   
3. Session Management: This because Passport.js relies on sessions to maintain user login state across requests. 
   - also added passport.serializeUser and passport.deserializeUser for session management.
```bash
npm install express-session
```
>[!Note]- `express-session`
>encountered the "Login sessions require session support" error
  
4. Backend Token Verification Endpoint: To handle the ID token sent from the frontend
```bash
npm install google-auth-library
```
- Then, created a new POST endpoint `/google-login`.
```js
app.post('/google-login', async (req, res) => {}
```
- This endpoint receives the **Google ID token**, using `google-auth-library` it securely verifies it with Google, and then sends a `success` response back to your frontend.
```js
const { credential } = req.body;
const ticket = await client.verifyIdToken({
        idToken: credential,
        audience: GOOGLE_CLIENT_ID, 
    });
```

```js
  try {
    const payload = ticket.getPayload();
    const userid = payload['sub'];
    res.json({ message: 'Login successful', user: payload });
  } catch (error) {
    console.error('Error verifying Google ID token:', error);
    res.status(401).json({ error: 'Authentication failed' });
  }
```

5. CORS Resolution:  occured "Cross-Origin-Opener-Policy" and "No 'Access-Control-Allow-Origin' header" errors,  
```bash
npm install cors
```
```js
const cors = require('cors');
app.use(cors());
```
*This allowed your frontend (running on http://localhost:4321) to make requests to your backend (running on http://localhost:3000).*


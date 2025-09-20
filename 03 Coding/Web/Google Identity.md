---
id: Google Identity
aliases: []
tags:
  - coding
  - web
dg-publish: true
---
# Google Identity

It is an implementation of Federated Identity Management (FIM) that allows users to sign in to third-party applications using their Google account credentials.
![[Pasted image 20250629205317.png]]

## Implementation

1. Configuration
2. Initialization
3. Rendering a Button
4. Signing In
5. Geting Profile Information
6. Signing Out

### Configuration

- Go to googles [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project or select an existing one.
- add a credential
- Configure Consenst screen and Create a OAuth 2.0 Client ID

### Initialization

```html
<meta
  name="google-signin-client_id"
  content="YOUR_CLIENT_ID.apps.googleusercontent.com"
/>

```

#### Using Node

   1. Receives a Google ID token from the frontend.
   2. Verifies that token with Google to ensure its authenticity.
   3. Extracts the user's profile information (ID, name, email, picture).
   4. Sends this verified user information back to your frontend.

```js
const express = require("express");
const { OAuth2Client } = require("google-auth-library");
const cors = require("cors");

const app = express();
const port = 3000;

const CLIENT_ID =
  "648118709365-es66btc3rfvbhf6hhbs3v0vr4p3tki8f.apps.googleusercontent.com";
const client = new OAuth2Client(CLIENT_ID);

app.use(express.json());
// NOTE: On the older server it was only available for the frontend
app.use(cors()); // Enable CORS for all origins

app.post('/google-login', async (req, res) => {
  const { token } = req.body;

  if (!token) {
    return res.status(400).json({ error: 'No token provided' });
  }

  try {
    const ticket = await client.verifyIdToken({
      idToken: token,
      audience: CLIENT_ID,
    });
    const payload = ticket.getPayload();
    const userid = payload['sub'];
    console.log('User ID:', userid);
    // You can now use the payload to get user information
    // For example: payload.name, payload.email, payload.picture
    res.status(200).json({
      message: 'Login successful',
      user: {
        id: userid,
        name: payload.name,
        email: payload.email,
        picture: payload.picture,
      },

    });
  } catch (error) {
    console.error('Error verifying Google ID token:', error);
    res.status(401).json({ error: 'Invalid token' });
  }
});

app.listen(port, () => {
  console.log(`Backend server listening at http://localhost:${port}`);
});

```

 
---
id: 02 Login Feature
aliases: 
tags:
  - sub_note
  - es_website
  - backend
dg-publish: true
---

# Login

- [[#Steps]]
  In order to facilitate the login feature , a backend server is needed.

## Steps

1.  Frontend - Google Identity Services (GIS) Library
    (`src/layouts/MainLayout.astro`):
    - I added the official Google Identity Services client library script
      (https://accounts.google.com/gsi/client) to your MainLayout.astro. This
      library handles rendering the Google Sign-In button and managing the ID
      token flow.

2.  Frontend - Login Modal (`src/components/ui/forms/LoginModal.astro`):
    - I removed the old GoogleBtn component from the modal.
    - I added specific div elements (g_id_onload and g_id_signin) with data-\*
      attributes (like data-client_id and data-callback) as required by GIS.
      GIS uses these divs to automatically render the Google Sign-In button.
    - The data-callback attribute was set to handleCredentialResponse, which is
      a global function that GIS will call after a successful sign-in.

3.  Frontend - Rewritten Authentication Script (`src/assets/scripts/auth.js`):
    - I completely rewrote this script to align with the GIS ID token flow.
    - `handleCredentialResponse` function: This global function now receives
      the Google ID token. It then fetches your new backend's /google-login
      endpoint, sending the ID token in the request body.
    - User Data Handling: Upon a successful response from your backend, it
      parses the user data.
    - Local Storage: It stores the user's profile information in localStorage
      for client-side persistence across page loads.
    - `updateUI` function: This helper function was created to manage the
      visibility of the login-button and user-info containers and populate
      user-info with the logged-in user's name and a logout button.
    - Logout Functionality: A logout function was added to clear localStorage
      and update the UI.
    - Initialization: The script now checks localStorage on DOMContentLoaded to
      determine the initial login state and update the UI accordingly.

4.  Frontend - Image Display Fixes (Unrelated to Auth, but happened during this
    period):
    - During the authentication integration, we also debugged and fixed issues
      with image display for product/project items, primarily related to
      incorrect file paths and Image component format attributes.

---

@begin Links
"Get started to configure your application's identity and manage credentials for calling Google APIs and Sign-in with Google" ?

- https://console.cloud.google.com/auth/clients?inv=1&invt=Ab1ZSA&project=iot-registration-gcek
-

@end Links

```
app_name: es_website
email: aruncs31ss@gmail.com
```

## Backend

Google Cloud Platform

1. Go to the Google API Console (https://console.developers.google.com/)
   and create a new project.
2. Go to the "Credentials" page.
3. Click "Create credentials" and select "OAuth client ID". _before this you need to to do [this](^pre_credentials_page)_
4. Select "Web application" as the application type.
5. Add http://localhost:3000 to the "Authorized JavaScript origins" and
   http://localhost:3000/auth/google/callback to the "Authorized
   redirect URIs".
6. Click "Create" and copy the "Client ID" and "Client secret".

</br>

@begin pre_credentials_page

1. Go to the OAuth Consent Screen page: You should see a prompt to
   configure it. -> When i clicked it took me to Branding page.

```
app_name: ES_Website
mail: aruncs31ss@gmail.com
```

2. Choose User Type:

- Select "External". This will allow any user with a Google account
  to use your application.
- Click "Create".

3. Fill out the App Information:

- App name: Enter the name of your application (e.g., "My Awesome
  App").
- User support email: Select your email address.
- Developer contact information: Enter your email address.

4. Save and Continue: You can leave the other fields blank for now.
   Click "Save and Continue" through the "Scopes" and "Test users"
   sections. You don't need to add anything there for now.
5. Review and go back to the dashboard: On the summary page, you can
   just review the information and then navigate back to the
   "Credentials" tab on the left-hand menu.

```
client_id: 648118709365-es66btc3rfvbhf6hhbs3v0vr4p3tki8f.apps.googleusercontent.com
```

2. CORS Error

The error Access to fetch at 'http://localhost:3000/user' from origin 'http://localhost:4321' has been blocked by CORS policy is a security measure
built into web browsers. It prevents a web page from making requests to a different domain (in this case, your Astro site at localhost:4321 is trying
to talk to your Express server at localhost:3000).

```js
const cors = require("cors");
app.use(
  cors({
    origin: "http://localhost:4321", // Allow requests from the frontend
    credentials: true, // Allow cookies to be sent
  }),
);
```

---
id: backend
aliases: 
tags:
  - es_website
  - backend
---
- [[Flask Backend]]
- Using [[Web3 Based Backend]]   👎
- using [[pennybase]] 👎
## code-id-0


```js
const cors = require("cors");
require("dotenv").config();
const express = require("express");
const session = require("express-session");
const passport = require("passport");
const GoogleStrategy = require("passport-google-oauth20").Strategy;

const app = express();

app.use(
  cors({
    origin: "http://localhost:4321",
    credentials: true,
  }),
);
app.use(express.static("public"));

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
  }),
);

app.use(passport.initialize());
app.use(passport.session());

passport.serializeUser((user, done) => {
  done(null, user);
});

passport.deserializeUser((user, done) => {
  done(null, user);
});

passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      callbackURL: "/auth/google/callback",
    },
    (accessToken, refreshToken, profile, done) => {
      return done(null, profile);
    },
  ),
);

app.get(
  "/auth/google",
  passport.authenticate("google", { scope: ["profile", "email"] }),
);

app.get(
  "/auth/google/callback",
  passport.authenticate("google", { failureRedirect: "/" }),
  (req, res) => {
    res.redirect("http://localhost:4321/");
  },
);

app.get("/user", (req, res) => {
  console.log("User request received:", req.user);
  if (req.user) {
    res.json(req.user);
  } else {
    res.json(null);
  }
});

app.get("/logout", (req, res) => {
  req.logout(function (err) {
    if (err) {
      return next(err);
    }
    res.redirect("/");
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

## Integrating with Database 
database (e.g., MongoDB, PostgreSQL, MySQL, SQLite) with a users collection or table,
  ==where each row/document represents a single user.==

  When a user signs in with Google, you would:
   1. Check for existing user: Query your users table/collection using their
      Google ID (sub from the payload) or email address.
   2. Create new user (if not exists): If no user is found, create a new record
      for them, storing their Google ID, name, email, picture, and any other
      relevant information.
   3. Update existing user (if exists): If the user already exists, you might
      update their last login time or any other profile information that Google
      provides and you want to keep in sync.

  To help you with this, could you tell me which database technology you'd
  prefer to use? Some common choices for Node.js applications include:


   * MongoDB: A NoSQL document database, often used with Mongoose ODM.
   * PostgreSQL/MySQL: Relational databases, often used with ORMs like Sequelize
     or Prisma, or a direct client like pg for PostgreSQL.
   * SQLite: A file-based relational database, good for simpler applications or
     local development, used with sqlite3.


  Once you choose, I can provide a more detailed plan and code examples.



---
id: user_model
aliases: []
tags: []
---

```js
import User, { USER_ROLES, USER_STATUS } from "../models/user";

const user = User.fromAPI(apiResponse);

if (user.isAdmin() && user.isActive()) {
  // Allow admin action
}

// Get display info
const avatar = user.getAvatarUrl();
const displayName = user.getDisplayName();

// Validate
const { valid, errors } = user.validate();

// Update
user.update({ status: USER_STATUS.SUSPENDED });

// Convert to JSON for API
const userData = user.toJSON();
```

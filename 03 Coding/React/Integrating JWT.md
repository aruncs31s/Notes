---
id: Integrating_JWT
aliases: []
tags:
  - coding
  - react
dg-publish: true
---
# Integrating JWT 

```js
const handleLoginSubmit = async () => {
  setLoading(true);
  setErrors({});

  const newErrors = {};
  if (!loginData.email) newErrors.email = 'Email is required';
  else if (!validateEmail(loginData.email)) newErrors.email = 'Invalid email format';
  
  if (!loginData.password) newErrors.password = 'Password is required';

  if (Object.keys(newErrors).length > 0) {
    setErrors(newErrors);
    setLoading(false);
    return;
  }

  try {
    const response = await fetch("http://localhost:9999/api/user/login", {
      method: "GET", // as per your API
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: loginData.email,
        password: loginData.password,
      }),
    });

    if (!response.ok) {
      throw new Error("Invalid email or password!");
    }

    const data = await response.json();
    const token = data.token;

    // Decode JWT
    const decoded = jwtDecode(token);

    // Save token and user info
    localStorage.setItem("token", token);
    localStorage.setItem("currentUser", JSON.stringify(decoded));

    setCurrentUser(decoded);
    setIsAuthenticated(true);
    navigate("/");

  } catch (err) {
    alert(err.message || "Login failed!");
  } finally {
    setLoading(false);
  }
};

```

## Registration 

```jsx
const handleSignupSubmit = async () => {
  setLoading(true);
  setErrors({});

  const newErrors = {};
  if (!signupData.fullName.trim()) newErrors.fullName = 'Name is required';
  if (!signupData.email) newErrors.email = 'Email is required';
  else if (!validateEmail(signupData.email)) newErrors.email = 'Invalid email format';
  if (!signupData.password) newErrors.password = 'Password is required';
  if (!signupData.confirmPassword) newErrors.confirmPassword = 'Please confirm your password';
  if (signupData.password !== signupData.confirmPassword) newErrors.confirmPassword = 'Passwords do not match';

  if (Object.keys(newErrors).length > 0) {
    setErrors(newErrors);
    setLoading(false);
    return;
  }

  try {
    const response = await fetch("http://localhost:9999/api/user/login", {
      method: "POST", // your API uses POST for signup
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: signupData.email,
        password: signupData.password,
        name: signupData.fullName,
      }),
    });

    if (!response.ok) {
      throw new Error("Signup failed!");
    }

    const data = await response.json();
    const token = data.token;

    // Decode JWT
    const decoded = jwtDecode(token);

    // Save token and user info
    localStorage.setItem("token", token);
    localStorage.setItem("currentUser", JSON.stringify(decoded));

    setCurrentUser(decoded);
    setIsAuthenticated(true);
    navigate("/");

  } catch (err) {
    alert(err.message || "Signup failed!");
  } finally {
    setLoading(false);
  }
};

```

## Logout

```js
const handleLogout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("currentUser");
  setIsAuthenticated(false);
  setCurrentUser(null);
  navigate("/login");
};

```
---
aliases:
  - es backend flask api
tags:
  - "#python"
  - api
  - flask
---
# Flask APIs
It this we should need the following `API's
1. `/api/register` - To register new users
2. `/api/login` - To login users
3. `/api/logout` - To logout users
4. `/api/user` - To get user details
5. `/api/upload-picture` - To upload profile picture


## Logins

> [!tip]- ##### `/api/login` 
> ```python
> 
> @app.route("/login", methods=["POST"])
> def login():
>     data = request.get_json()
>     email = data.get("email")
>     password = data.get("password")
>     user = User.query.filter_by(email=email).first()
> 
>     if not user or not check_password_hash(user.password, password):
>         print("Invalid email or password.")
>         return jsonify({"status": "error", "message": "Invalid credentials"}), 401
>     session["email"] = user.email
>     return jsonify({"status": "success", "message": "Login successful!"}), 200
> 
> ```

@requires 
```json
{
"name": "",
"email": "",
"password": ""
}
```


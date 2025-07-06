---
id: 02 Flask APIs
aliases:
  - es backend flask api
tags:
  -  #python
  - api
  - flask
---

# Flask APIs
>[!blank|right-small]+ Table of Contents
>    - [[02 Flask APIs#Logins|Logins]]
>    - [[02 Flask APIs#Session|Session]]
>        - [[02 Flask APIs#Implementation|Implementation]]
>    - [[02 Flask APIs#Picture upload|Picture upload]]


It this we should need the following `API's

1. `/api/register` - To register new users
2. [`/api/login` - To login users
3. `/api/logout` - To logout users
4. `/api/user` - To get user details
5. `/api/upload-picture` - To upload profile picture

## Logins

> [!tip]- ##### _api:_ `/api/login`
>
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

> [!check]+ **Test `/api/login`**
>
> ```bash
>  curl -v -X  POST http://127.0.0.1:5000/api/login \
> -H "Content-Type: application/json" \
> -d '{
>  "password": "simplepass", "email": "test@gmail.com"}'
> ```

> ☑ few things to consider
>
> 1. `Content-Type: application/json`
> 2. `Set-Cookie: session=eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIn0.aGr_AA.YPS7NYQnu1Iwb3x-zSAoGv_4SbA; HttpOnly; Path=/`
> 3. `{ "message": "Login successful!", "status": "success" }`

## Session

Session is required to keep the user logged in after login.

### Implementation

```python
from flask import session

@app.route("/api/login")
def login():
    session["email"] = user.email
```

> **Checking**
>
> ```python
> user = User.query.filter_by(email=session["email"]).first()
> ```

> [!abstract]- _api:_ root `/`
>
> ```python
> @app.route("/")
> def index():
>     if "email" in session:
>         user = User.query.filter_by(email=session["email"]).first()
>         if user:
>             return jsonify(
>                 {"status": "success", "user": {"name": user.name, "email": user.email}}
>             )
>     return jsonify({"status": "error", "message": "Not logged in"}), 401
> ```

> [!check]+ **Test `root` `/`**
>
> ```bash
> curl -s http://localhost:5000/ \
> --cookie "session=eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIn0.aGr_AA.YPS7NYQnu1Iwb3x-zSAoGv_4SbA"
> ```
>
> ```json
> {
>   "status": "success",
>   "user": {
>     "email": "test@gmail.com",
>     "name": "aruncs"
>   }
> }
> ```

It seems the session is working

## Picture upload


> [!abstract]+ _api:_ `/upload_profile_pic`
>
> ```python
>
> @app.route("/upload_profile_pic", methods=["POST"])
> def upload_profile_pic():
>     if "email" not in session:
>         return jsonify({"status": "error", "message": "Unauthorized"}), 401
>
>     user = User.query.filter_by(email=session["email"]).first()
>     if not user:
>         return jsonify({"status": "error", "message": "User not found"}), 404
>
>     file = request.files.get("profile_pic")
>     if not file or file.filename == "":
>         return jsonify({"status": "error", "message": "No file uploaded"}), 400
>     if not allowed_file(file.filename):
>         return jsonify({"status": "error", "message": "Invalid file type"}), 400
>
>     # Save file
>     filename = secure_filename(file.filename)
>     new_filename = f"{user.id}_{filename}"
>     filepath = os.path.join(app.config["UPLOAD_FOLDER"], new_filename)
>     file.save(filepath)
>
>     # Optional: delete old pic file if needed (not required)
>     user.profile_pic = new_filename
>     db.session.commit()
>
>     return (
>         jsonify(
>             {
>                 "status": "success",
>                 "message": "Profile picture updated",
>                 "profile_pic_url": url_for(
>                     "uploaded_file", filename=new_filename, _external=True
>                 ),
>             }
>         ),
>         200,
>     )
>
> ```


> [!check]+ **Test upload**
> ```bash
>  curl -X POST http://localhost:5000/upload_profile_pic \
>   -F "profile_pic=@test.png" \
>   --cookie "session=eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIn0.aGr_AA.YPS7NYQnu1Iwb3x-zSAoGv_4SbA"
> ```
> 






```json
{
  "message": "Profile picture updated",
  "profile_pic_url": "http://localhost:5000/uploads/2_test.png",
  "status": "success"
}

```

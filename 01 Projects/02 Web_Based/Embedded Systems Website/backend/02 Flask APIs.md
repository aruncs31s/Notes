---
id: 02 Flask APIs
aliases:
  - es backend flask api
tags:
  - api
  - flask
  - es_website
  - backend
---

# Flask APIs
>[!blank]
>- [x] `/api/login` ✅ 2025-07-10
>- [x] `/api/regster` ✅ 2025-07-10
>- [x] `/api/upload_profile_pic` ✅ 2025-07-10
>- [x] `/api/logout` ✅ 2025-07-10

## Authentication
> [!tip]- ##### _api:_ `/api/login`
>
> ```python
>
> @app.route("/api/login", methods=["POST"])
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
>
> > [!check]+ **Test `/api/login`**
> >
> > ```bash
> >  curl -v -X  POST http://127.0.0.1:5000/api/login \
> > -H "Content-Type: application/json" \
> > -d '{
> >  "password": "simplepass", "email": "test@gmail.com"}'
> > ```

> [!abstract]- ##### _api:_ root `/`
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
>
> > [!check]- **Test `root` `/`**
> >
> > ```bash
> > curl -s http://localhost:5000/ \
> > --cookie "session=eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIn0.aGr_AA.YPS7NYQnu1Iwb3x-zSAoGv_4SbA"
> > ```
> >
> > ```json
> > {
> >   "status": "success",
> >   "user": {
> >     "email": "test@gmail.com",
> >     "name": "aruncs"
> >   }
> > }
> > ```

> [!abstract]+ ##### _api:_ `/upload_profile_pic`
>
> ```python
>
> @app.route("/api/upload_profile_pic", methods=["POST"])
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
>
> > [!check]+ **Test `/upload_profile_pic`**
> >
> > ```bash
> >  curl -X POST http://localhost:5000/upload_profile_pic \
> >   -F "profile_pic=@test.png" \
> >   --cookie "session=eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIn0.aGr_AA.YPS7NYQnu1Iwb3x-zSAoGv_4SbA"
> > ```
> >
> > > [!success]+ **`response`**
> > >
> > > ```json
> > > {
> > >   "message": "Profile picture updated",
> > >   "profile_pic_url": "http://localhost:5000/uploads/2_test.png",
> > >   "status": "success"
> > > }
> > > ```

> [!abstract]- ##### ***api:*** `/register`
> ```python
> @app.route("/api/register", methods=["POST"])
> def register():
>     data = request.get_json()
>     name = data.get("name")
>     email = data.get("email")
>     password = data.get("password")
>     if not name or not email or not password:
>         return jsonify({"status": "error", "message": "All fields are required"}), 400
>     if email:
>         existing_user = User.query.filter_by(email=email).first()
>     if existing_user:
>         return jsonify({"status": "error", "message": "Email already registered"}), 400
>     hashed_password = generate_password_hash(password)
>     new_user = User(name=name, email=email, password=hashed_password)
>     try:
>         db.session.add(new_user)
>         db.session.commit()
>     except Exception as e:
>         db.session.rollback()
>         return jsonify({"status": "error", "message": str(e)}), 500
>     return jsonify({"status": "success", "message": "User registered successfully"}), 201
> ```
> > [!check]+ Test `/api/register`
> > ![[curl POST examples#^00546a]]
> >
> > >[!success]- `response`
> > >```json
> > >{
  "message": "User registered successfully",
  "status": "success"
>>>}
>>>```


### Login

#### Using Node 

```js
async function fetchData() {
    const url = 'http://localhost:5000';
    const response = await fetch(url + '/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: 'testuser@example.com', password: 'password123' }),
    });
    const data = await response.json();
    console.log(data);
}

fetchData();
```

#### Using Curl 
```bash
url="http://localhost:5000"
curl -X POST "$url/api/login" \
  -H "Content-Type: application/json" \
  -d '{
  "email": "aruncs31ss@proton.me",
  "password": "pass1234"
}'
```

> [!success]- *response*
> ```json
> {
>   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3R1c2VyQGV4YW1wbGUuY29tIiwiZXhwIjoxNzUyMTQ5MDc4fQ.ogaKYkui9gCqr69uCSonri4i6hmbxXT0bDw__HyjQTI",
>   "message": "Login successful!",
>   "status": "success"
> }
> ```


### Register

#### Using Curl 

```bash
url="http://localhost:5000"
curl -vvX POST "$url/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Arun CS",
    "email": "aruncs31ss@proton.me",
    "password": "pass1234"
}'

```


> [!success]- *response*
> ```json
> {
>   "message": "User registered successfully",
>   "status": "success"
> }
> ```




## Content Upload


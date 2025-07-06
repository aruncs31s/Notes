# Flask Backend 
It should have  
- POST `/register `– for new users to sign up
- POST` /login` – to authenticate existing users
- GET `/profile` or similar – to get user data
- Optional: POST `/logout`


> [!success]+ **Test Code**
> ```python
> from flask import (Flask, flash, redirect, render_template, request, session,
>                    url_for)
> from flask_sqlalchemy import SQLAlchemy
> from werkzeug.security import check_password_hash, generate_password_hash
> 
> app = Flask(__name__)
> app.secret_key = "supersecretkey"
> app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
> app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
> db = SQLAlchemy(app)
> 
> 
> class User(db.Model):
>     id = db.Column(db.Integer, primary_key=True)
>     name = db.Column(db.String(100), nullable=False)
>     email = db.Column(db.String(100), unique=True, nullable=False)
>     password = db.Column(db.String(200), nullable=False)
>     role = db.Column(db.String(50), nullable=False)
> 
>     def __repr__(self):
>         return f"<User {self.email}>"
> 
> 
> @app.route("/")
> def index():
>     if "email" in session:
>         user = User.query.filter_by(email=session["email"]).first()
>         if user:
>             return render_template("index.html", user=user)
>     return render_template("index.html")
> 
> 
> @app.route("/register", methods=["POST"])
> def register():
>     name = request.form.get("name")
>     email = request.form.get("email")
>     password = request.form.get("password")
>     role = request.form.get("role")
> 
>     existing_user = User.query.filter_by(email=email).first()
>     if existing_user:
>         flash("Email already registered.", "danger")
>         return redirect(url_for("index"))
> 
>     hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
>     new_user = User(name=name, email=email, password=hashed_password, role=role)
>     db.session.add(new_user)
>     db.session.commit()
> 
>     flash("Registration successful! Please login.", "success")
>     return redirect(url_for("index"))
> 
> 
> @app.route("/login", methods=["POST"])
> def login():
>     email = request.form.get("email")
>     password = request.form.get("password")
> 
>     user = User.query.filter_by(email=email).first()
> 
>     if not user or not check_password_hash(user.password, password):
>         flash("Invalid credentials. Please try again.", "danger")
>         return redirect(url_for("index"))
> 
>     flash(f"Welcome, {user.name}!", "success")
>     session["email"] = user.email
>     return redirect(url_for("index"))
> 
> 
> @app.route("/logout", methods=["POST"])
> def logout():
>     session.pop("email", None)
>     flash("You have been logged out.", "info")
>     return redirect(url_for("index"))
> 
> 
> if __name__ == "__main__":
>     with app.app_context():
>         db.create_all()
>     app.run(debug=True)
> ```

## Routes 

> [!abstract]+ `/register`
> ```python
> @app.route("/register", methods=["POST"])
> def register():
>     name = request.form.get("name")
>     email = request.form.get("email")
>     password = request.form.get("password")
> 
>     existing_user = User.query.filter_by(email=email).first()
>     if existing_user:
>         flash("Email already registered.", "danger")
>         return redirect(url_for("index"))
> 
>     hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
>     new_user = User(name=name, email=email, password=hashed_password)
>     db.session.add(new_user)
>     db.session.commit()
> 
>     flash("Registration successful! Please login.", "success")
>     return redirect(url_for("index"))
> ```

It first gets `name` , `email` , `password` 

```python
name = request.form.get("name") 
email = request.form.get("email") 
password = request.form.get("password") 

```


```bash
curl -sX  POST http://127.0.0.1:5000/register \
-H "Content-Type: application/json" \
-d '{"name": "aruncs", "email": "aruncs31ss@gmail.com", "password": "simplepass"}' -v

```


> [!abstract]- Profile Pic not workig
> ```python
> import os
> 
> from flask import (Flask, flash, redirect, render_template, request, session,
>                    url_for)
> from flask_sqlalchemy import SQLAlchemy
> from werkzeug.security import check_password_hash, generate_password_hash
> from werkzeug.utils import secure_filename
> 
> app = Flask(__name__)
> app.secret_key = "supersecretkey"
> app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
> app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
> db = SQLAlchemy(app)
> 
> UPLOAD_FOLDER = "static/profile_pics"
> ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
> 
> app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
> 
> 
> def allowed_file(filename):
>     return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
> 
> 
> class User(db.Model):
> 
>     id = db.Column(db.Integer, primary_key=True)
>     name = db.Column(db.String(100), nullable=False)
>     email = db.Column(db.String(100), unique=True, nullable=False)
>     password = db.Column(db.String(200), nullable=False)
>     profile_pic = db.Column(db.String(255), nullable=True)
> 
>     def __repr__(self):
>         return f"<User {self.email}>"
> 
> 
> @app.route("/")
> def index():
>     if "email" in session:
>         user = User.query.filter_by(email=session["email"]).first()
>         if user:
>             return render_template("index.html", user=user)
>     return render_template("index.html")
> 
> 
> @app.route("/register", methods=["POST"])
> def register():
>     name = request.form.get("name")
>     email = request.form.get("email")
>     password = request.form.get("password")
> 
>     existing_user = User.query.filter_by(email=email).first()
>     if existing_user:
>         flash("Email already registered.", "danger")
>         return redirect(url_for("index"))
> 
>     hashed_password = generate_password_hash(password, method="pbkdf2:sha256")curl -sX POST http://192.168.31.92:5000/robots \
> -H "Content-Type: application/json" \
> -d '{"id": 1, "last_position": 45}'
>     print(hashed_password)
>     new_user = User(name=name, email=email, password=hashed_password, profile_pic=None)
>     db.session.add(new_user)
>     db.session.commit()
> 
>     flash("Registration successful! Please login.", "success")
>     return redirect(url_for("index"))
> 
> 
> @app.route("/login", methods=["POST"])
> def login():
>     email = request.form.get("email")
>     password = request.form.get("password")
> 
>     user = User.query.filter_by(email=email).first()
> 
>     if not user or not check_password_hash(user.password, password):
>         flash("Invalid credentials. Please try again.", "danger")
>         return redirect(url_for("index"))
> 
>     flash(f"Welcome, {user.name}!", "success")
>     session["email"] = user.email
>     return redirect(url_for("index"))
> 
> 
> @app.route("/profile")
> def profile():
>     if "email" not in session:
>         flash("Please log in to view your profile.", "danger")
>         return redirect(url_for("index"))
> 
>     user = User.query.filter_by(email=session["email"]).first()
>     if not user:
>         flash("User not found.", "danger")
>         return redirect(url_for("index"))
> 
>     return render_template("profile.html", user=user)
> 
> 
> @app.route("/logout", methods=["POST"])
> def logout():
>     session.pop("email", None)
>     flash("You have been logged out.", "info")
>     return redirect(url_for("index"))
> 
> 
> if __name__ == "__main__":
>     with app.app_context():
>         db.create_all()
>     app.run(debug=True)
> ```



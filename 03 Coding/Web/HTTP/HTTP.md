---
cssclasses:
  - wide-page
dg-publish: true
tags:
  - web
  - http
---

### HTTP GET and POST Methods

HTTP methods define actions for interacting with web resources. Here's a simple explanation of GET and POST, two of the most common ones:

#### GET Method
- **Purpose**: Retrieves data from the server without modifying it.
- **How it works**: Data is sent as part of the URL (query parameters), e.g., `http://example.com/search?q=python`.
- **Characteristics**:
  - Safe (doesn't change server state).
  - Idempotent (multiple identical requests have the same effect).
  - Can be cached by browsers and proxies.
  - Limited data size (URL length restrictions).
- **Use cases**: Fetching pages, searching, reading data.

#### POST Method
- **Purpose**: Sends data to the server to create, update, or process resources.
- **How it works**: Data is sent in the request body (not visible in URL), e.g., form submissions or JSON payloads.
- **Characteristics**:
  - Not safe (can modify server state).
  - Not idempotent (repeated requests might create duplicates).
  - Not cached by default.
  - No size limits (can send large data).
- **Use cases**: Submitting forms, uploading files, creating accounts.

### Flask Examples

Flask is a lightweight Python web framework. Below are simple examples for handling GET and POST requests. Install Flask first: `pip install flask`.

#### GET Example
This route responds to GET requests and returns a simple message.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')  # Get 'name' from query params
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
```

- **Usage**: Visit `http://localhost:5000/greet?name=Alice` → Returns "Hello, Alice!"
- **Explanation**: Uses `request.args` to access URL parameters.

#### POST Example
This route handles POST requests, processes form data, and responds.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')  # Get 'username' from form data
    if username:
        return f"Welcome, {username}!"
    return "No username provided", 400

if __name__ == '__main__':
    app.run(debug=True)
```

- **Usage**: Send a POST request with form data (e.g., via a form or tool like Postman) to `http://localhost:5000/submit` with `username=Bob` → Returns "Welcome, Bob!"
- **Explanation**: Uses `request.form` to access submitted data. For JSON, use `request.get_json()`.

Run these in a Python file (e.g., `app.py`) and start with `python app.py`. For production, add security like CSRF protection.
---
id: CORS
aliases: []
tags:
  - coding
  - web
dg-publish: true
---
# CORS
**SOP**: Same Origin Policy is a security measure that prevents a web page from making requests to a different domain than the one that served the web page.
**CORS**: Cross-Origin Resource Sharing is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served.

- [ ] complete this https://youtu.be/E6jgEtj-UjI?si=CDk48ZjkkroJiMkg

### CORS in Express.js

```js
const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors()); // Enable CORS for all routes

app.get('/api/data', (req, res) => {
	res.json({ message: 'This is CORS-enabled for all origins!' });
});
app.listen(3000, () => {
	console.log('CORS-enabled web server listening on port 3000');
});

```

## CORS Headers

- `Access-Control-Allow-Origin`: Specifies which origins are allowed to access the resource.
- `Access-Control-Allow-Methods`: Specifies which HTTP methods are allowed when accessing the resource.
- `Access-Control-Allow-Headers`: Specifies which headers can be used when making the actual request.
- `Access-Control-Allow-Credentials`: Indicates whether the browser should include credentials (cookies, HTTP authentication) in the request.
- `Access-Control-Expose-Headers`: Indicates which headers can be exposed as part of the response.
- `Access-Control-Max-Age`: Indicates how long the results of a preflight request can be cached.
- `Access-Control-Request-Method`: Used in preflight requests to indicate which HTTP method will be used in the actual request.
- `Access-Control-Request-Headers`: Used in preflight requests to indicate which headers will be used in the actual request.
- `Origin`: Indicates the origin of the request, which is sent in both simple and preflight requests.
- `Vary`: Indicates that the response varies based on the `Origin` header, which is important for caching.
- `Access-Control-Request-Private-Network`: Indicates whether the request is a private network request, which is relevant for security considerations.
- `Access-Control-Request-Private-Network-Allowed`: Indicates whether the request is allowed to access private network resources.
- `Access-Control-Request-Private-Network-Not-Allowed`: Indicates that the request is not allowed to access private network resources.
- `Access-Control-Request-Private-Network-Allowed-Reason`: Provides a reason for why the request is allowed or not allowed to access private network resources.
- `Access-Control-Request-Private-Network-Not-Allowed-Reason`: Provides a reason for why the request is not allowed to access private network resources.
- `Access-Control-Request-Private-Network-Allowed-By-Default`: Indicates whether the request is allowed by default to access private network resources.
- `Access-Control-Request-Private-Network-Not-Allowed-By-Default`: Indicates whether the request is not allowed by default to access private network resources.
- `Access-Control-Request-Private-Network-Allowed-By-Default-Reason`: Provides a reason for why the request is allowed by default to access private network resources.
- `Access-Control-Request-Private-Network-Not-Allowed-By-Default-Reason`: Provides a reason for why the request is not allowed by default to access private network resources.
- 
```go
	r.Use(cors.New(cors.Config{
		AllowOriginFunc: func(origin string) bool {
			return strings.HasSuffix(origin, "localhost") ||
				origin == "https://etlab-backend-go.onrender.com" ||
				origin == "http://localhost:4200" ||
				origin == "http://192.168.29.111:4200"
		},
		AllowMethods:     []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowHeaders:     []string{"Origin", "Content-Type", "Authorization", "sentry-trace", "baggage"},
		ExposeHeaders:    []string{"Content-Length", "Access-Control-Allow-Origin", "Access-Control-Allow-Headers", "Content-Type"},
		AllowCredentials: true,
	}))
	// JWT Middleware
	r.Use(middleware.SetCors())
```
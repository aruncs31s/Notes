---
id: HTTP_Status_Codes
aliases: []
tags:
  - os
  - tools
  - networking
  - http
dg-publish: true
---
## 2xx Success

| Code  | Meaning    | Usage                                                         |
| ----- | ---------- | ------------------------------------------------------------- |
| `200` | OK         | Standard success response.                                    |
| `201` | Created    | Something was successfully created (e.g., a user, post, etc). |
| `202` | Accepted   | Request accepted but processing is not complete.              |
| `204` | No Content | Success, but no content returned (e.g., after DELETE).        |

## 3xx Redirect
|Code|Meaning|Usage|
|---|---|---|
|`301`|Moved Permanently|URL has permanently changed.|
|`302`|Found (Moved Temporarily)|Temporary redirection.|
|`304`|Not Modified|Used for caching — no need to resend data.|

## 4xx Client Errors
| Code  | Meaning              | Usage                                                                   |
| ----- | -------------------- | ----------------------------------------------------------------------- |
| `400` | Bad Request          | Request is malformed (e.g., invalid JSON, missing fields).              |
| `401` | Unauthorized         | Authentication failed (e.g., wrong password, no token).                 |
| `403` | Forbidden            | Authenticated but not allowed to access resource.                       |
| `404` | Not Found            | Resource doesn't exist.                                                 |
| `405` | Method Not Allowed   | Method (e.g., POST vs GET) not allowed for this endpoint.               |
| `409` | Conflict             | Conflict in resource state (e.g., duplicate email).                     |
| `422` | Unprocessable Entity | Valid data structure but semantically wrong (e.g., password too short). |

## 5xx Server Errors
|Code|Meaning|Usage|
|---|---|---|
|`500`|Internal Server Error|General server error — unexpected crash.|
|`502`|Bad Gateway|Server received invalid response from upstream.|
|`503`|Service Unavailable|Server temporarily unavailable (e.g., overloaded).|
|`504`|Gateway Timeout|Server timeout from upstream server.|

### With Flask

```python
return jsonify({"status": "success"}), 200
return jsonify({"status": "created"}), 201
return jsonify({"error": "Invalid input"}), 400
return jsonify({"error": "Unauthorized"}), 401
return jsonify({"error": "Forbidden"}), 403
return jsonify({"error": "Not found"}), 404
return jsonify({"error": "Already exists"}), 409
return jsonify({"error": "Server error"}), 500

```
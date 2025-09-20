---
id: flask file server
aliases: []
tags:
  - os
  - tools
  - server
Date: "2024-08-04"
dg-publish: true
---
# flask file server

## Contents

- [[#Authention]]

### Authention

Authention is provided in the code in the form of `user:passwd` so i have to encode the key=user:passwd using openssl

```bash
echo -n 'user:passwd' | openssl base64

```

## References

- [source](https://github.com/Wildog/flask-file-server)

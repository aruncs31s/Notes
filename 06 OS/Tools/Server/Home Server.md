---
id: Server
aliases:
  - home server
tags: []
---

# Home Server

> [!note|right-small] Contents
>
> - [[#Steps i had to take]]
> - Setup
> - [[flask file server]]
> - [[#Routing]]

Server Side

- Reverse Proxy and Routing

#### Objective

My objective is to make a server that can be accessible trough a web browser and it should support uploading files

- User : [This repo](https://github.com/Wildog/flask-file-server?tab=readme-ov-file)

#### Steps I had to take

1.  turn on usb tethering on my `OP`
2.  go to `network manager`(nm-applet) -> any_ethernet network settings -> Share this computer internet ->
3.  IP configuration _This entirely depend on the router_

```json
config {
ip: 192.168.1.2
subnet: 24 or 255.255.255.255,
gateway: 192.168.1.1
	}
```

4. Goto `flask-file-server` directory

```bash
cd flask-file-server
```

5. Change the environment variables

```bash
# nvim .env
FS_PATH=
FS_KEY=
FS_BIND=0.0.0.0
FS_PORT=8000
```

- where `FS_PATH` is the serving path
- `FS_KEY` should be in the format [[flask file server#authention]]

6. start the server

```bash
python file-server.py
```

- This will start the web server in the specified port but in order it brings a new problem user have to type `ip:port` to reach it instead of making it like that we can `port forward` the port to , when ever the user types `ip` it should point to `ip:port`. To overcome this do the following

7. Port Forwarding

I'm using [[iptables]] to port forward

- [x] Later need to switch to [[nginx]]

##### Nginx

```bash
# sudo nvim /etc/nginx/nginx.conf
server {
    listen 80;
    server_name domain name; # eg:192.168.1.1
    location / {
        proxy_pass http://127.0.0.1:8000; # flask app running port(address)
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

This should be inside the `http` context

8. Now Test the `nginx` config and restart the `nginx` service
   Test:

```bash
sudo nginx -t
```

Restart:

```bash
sudo systemctl restart nginx
```

_need to enable the service if not already enabled_

## References

- [[IP Forwarding]] : Enabling IP Forwarding
-

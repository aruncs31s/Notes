---
id: FreshRss
aliases: []
tags: []
---

```bash
sudo pacman -Syu
sudo pacman -S php php-fpm php-cgi php-gd php-intl php-tidy php-xmlrpc php-curl php-mbstring php-mcrypt php-pdo php-sqlite
```

- /etc/nginx/config.d/freshrss.conf

```bash
server { listen 80; server_name freshrss.example.com; root /var/www/html/freshrss; index index.php; location / { try_files $uri /index.php$is_args$args; } location ~ \.php$ { include fastcgi.conf; fastcgi_pass unix:/run/php-fpm/php-fpm.sock; } }
```

#!/usr/bin/env bash
# Bash script that sets up your web servers
# for the deployment of web_static

# install ngnix if not exists
# install prerequisites
sudo apt update
sudo apt install -y nginx
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "\
<html>
  <head>
  </head>
  <body>
ALX
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
	listen 80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 http://cuberule.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default

service nginx restart

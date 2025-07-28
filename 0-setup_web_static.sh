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
mkdir /localhost/
mkdir /localhost/hbnb_static
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default
service nginx restart

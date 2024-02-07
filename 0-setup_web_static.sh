#!/usr/bin/env bash
# This script sets up web servers for the deployment of web-static

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo -e "<html>\n\t<head></head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tserver_name _;$/a\\\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
service nginx restart

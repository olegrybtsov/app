#/bin/bash
mkdir my_app
cd my_app
git clone https://github.com/olegrybtsov/app.git
mv app/config/server.py ./
mv app/config/wsgi.py ./
mv app/config/nginx.conf /etc/nginx/nginx.conf -f

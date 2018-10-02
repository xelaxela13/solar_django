# Solar_django
Landing page on Django

For Mysql, install before requirements
---------
sudo apt-get install python3-dev libmysqlclient-dev build-essential

Requirements
------------
Requirements generate for pip-tools, from requirements.in file

pip install pip-tools

pip-compile requirements.in

Translater
----------
Add yours translations in /local/ru/LC_MESSAGES/django.po file and after that compile it using www.yourdomain.com/rosetta link

Passwords and Keys
------------------
It will search for a local file named .env to set the configuration variables and will fall back to the environment variables. It also provides an interface to define default values, transform the data into int, bool, and list when applicable. https://pypi.org/project/python-decouple/

pip install python-decouple

in /settings.py

from decouple import config

SECRET_KEY = config('SECRET_KEY')

To be create default .env file run:

python set_env_vars.py

Heroku deploy
-------------
1. Uncomment Heroku settings in settings.py

2. Push to GitHub

3. On Heroku dashboard

    3.1 connect to GitHub and deploy manual

    3.2 settings Config Variables - add SECRET_KEY, DATABASE_URL(heroku db url), IPSTACK_ACCESS_KEY etc. all yours app variables

4. heroku login

5. heroku run manage.py migrate

6. heroku run manage.py createsuperuser

7. heroku open

Start wsgi using gunicorn
-------------------------
sudo gunicorn -c gunicorn.py project.wsgi

Gmail settings
--------------

https://accounts.google.com/DisplayUnlockCaptcha

https://www.google.com/settings/security/lesssecureapps

Deploy to VPS using nginx + gunicorn
------------------------------------
In folder /home/USER/web/domain_name/public_html

1. git clone https://github.com/xelaxela13/solar_django.git
2. cd solar_django
3. virtualenv -p python3 ./virtenv
4. source ./virtenv/bin/activate
5. pip install -r requrements.txt
6. set_env_vars.sh
7. modify .env file - add to ALLOWED_HOSTS mydomain.com, localhost, 127.0.0.1
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04

7. copy gunicorn.service to /ets/systemd/system (fix PATHs)
8. nginx conf example
```
    server {
        listen      185.25.117.56:80;
        server_name iceberg.osf.com.ua www.iceberg.osf.com.ua;
        error_log  /var/log/httpd/domains/iceberg.osf.com.ua.error.log error;
        location / {
            proxy_pass      http://unix:/home/xela/web/iceberg.osf.com.ua/public_shtml/solar_django/project.sock;
            proxy_set_header X-Forwarded-Host $server_name;
            proxy_set_header X-Real-IP $remote_addr;
            add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
        location /static/ {
            autoindex on;
            alias /home/xela/web/iceberg.osf.com.ua/public_shtml/solar_django/asset/;
        }
        location /media/ {
            autoindex on;
            alias /home/xela/web/iceberg.osf.com.ua/public_shtml/solar_django/media/;
        }
        location /error/ {
            alias   /home/xela/web/iceberg.osf.com.ua/document_errors/;
        }
        location ~ /\.ht    {return 404;}
        location ~ /\.svn/  {return 404;}
        location ~ /\.git/  {return 404;}
        location ~ /\.hg/   {return 404;}
        location ~ /\.bzr/  {return 404;}
        if ($host ~* ^www\.(.*)$) {
           rewrite / $scheme://$1 permanent;
        include /home/xela/conf/web/nginx.iceberg.osf.com.ua.conf*;
    }
```
Docker
------
deploy.sh

OR

docker-compose build

docker-compose up -d

docker exec -it web python manage.py runserver 0:8080
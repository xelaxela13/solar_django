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

set_env_vars.sh

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
sudo gunicorn -c gunicorn_conf.py project.wsgi

Gmail settings
--------------

https://accounts.google.com/DisplayUnlockCaptcha

https://www.google.com/settings/security/lesssecureapps

Deploy to VPS using nginx
-------------------------
In folder /home/USER/web/domain_name/public_html

1. git clone https://github.com/xelaxela13/solar_django.git
2. cd solar_django
3. virtualenv -p python3 ./virtenv
4. source ./virtenv/bin/activate
5. pip install -r requrements.txt
6. set_env_vars.sh

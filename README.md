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

For create default .env file: python set_default_env_vars.py

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


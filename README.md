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
It will search for a local file named .env to set the configuration variables and will fall back to the environment variables. It also provides an interface to define default values, transform the data into int, bool, and list when applicable.

pip install python-decouple

in /settings.py

from decouple import config

SECRET_KEY = config('SECRET_KEY')


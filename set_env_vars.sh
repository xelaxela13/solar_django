#!/bin/sh
export SECRET_KEY=mysecretkey
source ./virtenv/bin/activate
python manage.py set_env_vars .env
unset SECRET_KEY
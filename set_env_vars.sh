#!/bin/sh
export SECRET_KEY=mysecretkey
python manage.py set_env_vars .env
unset SECRET_KEY
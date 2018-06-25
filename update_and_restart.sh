#! /usr/bin/env bash

source virtenv/bin/activate
git pull
pip install -r requirements.txt
python manage.py collectstatic
systemctl restart gunicorn
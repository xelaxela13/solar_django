#!/usr/bin/env bash

source "./virtenv/bin/activate"
gunicorn -c gunicorn_conf.py project.wsgi
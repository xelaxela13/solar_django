FROM python:3.6
ENV PYTHONUNBUFFERED 1
COPY . /srv/www/solar_django
WORKDIR /srv/www/solar_django
RUN pip install -r requirements.txt
RUN python set_env_vars.py
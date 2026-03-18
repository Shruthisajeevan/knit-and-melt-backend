#!/usr/bin/env bash

pip install -r requirements.txt

mkdir -p staticfiles

python manage.py collectstatic --noinput

python manage.py migrate

python manage.py loaddata api/fixtures/initial_data.json

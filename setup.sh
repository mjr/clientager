#!/bin/bash
virtualenv venv
source venv/bin/activate
venv/bin/pip install -r requirements.txt

pip install psycopg2

python3 manage.py makemigrations
python3 manage.py migrate

#!/bin/bash
virtualenv -p python3 venv
pip install --upgrade virtualenv
source venv/bin/activate

venv/bin/pip install -r requirements.txt

pip install psycopg2

python3 manage.py makemigrations
python3 manage.py migrate

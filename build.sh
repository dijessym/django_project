#!/usr/bin/env bash
<<<<<<< HEAD
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
=======
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
>>>>>>> a4f0de6f3c8a9d7d9db2e97a5b22f132eb9b7f28

#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
# para que en la nube, se instale esos requerimientos de mi proyecto, se saca con "pip freeze > requeriments.txt"
pip install -r requierements.txt
python manage.py collectstatic --no-input
python manage.py migrate
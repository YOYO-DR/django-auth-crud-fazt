#con este archivo ejecuto los comandos requeridos en el server de render, en el Build Command pongo ./build.sh
#le debo agregar en Environment/Environment Variables le agrego PYTHON_VERSION y pongo la version de python que estoy utilizando, 3.11.2 en este caso, asi, solo el numero
#creo la base de datos gratis de postgrest ahi en render, arriba en New, la creo y copio la Internal Database URL que me da, y en Environment/Environment Variables creo una que se llame DATABASE_URL y en el valor pego la llave interna que cree 
#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
# para que en la nube, se instale esos requerimientos de mi proyecto, se saca con "pip freeze > requeriments.txt"
pip install -r requirements.txt
python manage.py collectstatic --no-input
# python manage.py makemigration
python manage.py migrate
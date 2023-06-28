release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn contact_list_api.wsgi.py
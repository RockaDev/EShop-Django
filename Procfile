release: python manage.py migrate
web: gunicorn EShop.wsgi:application --log-file - --log-level debug
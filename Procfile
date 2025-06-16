release: python manage.py migrate
web: daphne --bind 0.0.0.0 --port $PORT project.asgi:application
worker: python manage.py runworker
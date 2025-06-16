release: python manage.py migrate
web: daphne --verbosity 0 --proxy-headers --bind 0.0.0.0 --port $PORT project.asgi:application
worker: python manage.py runworker --threads 4


web: python manage.py migrate && daphne -b 0.0.0.0 -p $PORT project.asgi:application
worker: python manage.py runworker websocket
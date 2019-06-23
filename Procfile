web: gunicorn sigma.wsgi

# Procfile with nginx, pgbouncer, gunicorn and django-q
web: bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c gunicorn.conf sigma.wsgi:application
worker: bin/start-pgbouncer-stunnel python manage.py qcluster

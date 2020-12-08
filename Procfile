release: pwd && ls
release: cd mysite
release: python manage.py migrate
web: gunicorn app.wsgi

echo "starting procfile..."
release: cd mysite && python manage.py migrate
web: gunicorn mysite.mysite.wsgi

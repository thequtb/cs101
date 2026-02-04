"""
WSGI-точка входа для продакшн-сервера (Gunicorn, uWSGI и т.д.).
При разработке используется manage.py runserver, этот файл не нужен.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

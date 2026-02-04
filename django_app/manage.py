#!/usr/bin/env python
"""
Точка входа для команд Django: runserver, migrate, createsuperuser и т.д.
Запуск: python manage.py <команда>
Перед этим нужно активировать виртуальное окружение (source venv/bin/activate).
"""
import os
import sys


def main():
    # Указываем Django, какой модуль настроек использовать (config/settings.py).
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django не найден. Установлен ли он в текущем окружении? "
            "Проверьте активацию venv и pip install -r requirements.txt."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

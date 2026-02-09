"""
Настройки Django-проекта config.
Главный файл конфигурации: БД, приложения, шаблоны, безопасность.
"""

from pathlib import Path

# Корень проекта (папка django_app). От него строятся пути к templates, static и т.д.
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для подписей (сессии, CSRF). В продакшене хранить в переменной окружения!
SECRET_KEY = 'django-insecure--s&w%6op@lh!*)*r)@fx9tdlh^^4_-*h5nh)0*2kssro82qm&3'

# Режим отладки: при True показываются подробные ошибки. В продакшене обязательно False.
DEBUG = True

# Список разрешённых имён хоста (Host заголовка). Запросы с другого Host будут отклонены.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'zere.shop']

# Подключённые приложения Django. auth — пользователи и авторизация, admin — админ-панель и т.д.
INSTALLED_APPS = [
    'sample',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Цепочка обработки каждого запроса: безопасность, сессии, CSRF, авторизация, сообщения.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Файл с корневыми маршрутами URL.
ROOT_URLCONF = 'config.urls'

# Настройки шаблонов: где искать HTML-файлы и какие контекст-процессоры подставляют переменные.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Наша папка templates в корне проекта
        'APP_DIRS': True,                  # Плюс папки templates внутри каждого приложения
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # В шаблонах доступна переменная user
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Подключение к PostgreSQL. Django создаёт таблицы через миграции (manage.py migrate).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cs101_db',
        'USER': 'cs101_owner',
        'PASSWORD': 'bismillah',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Валидаторы паролей при смене/создании пароля (сложность, длина и т.д.).
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Язык и часовой пояс интерфейса.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL-префикс для статики (CSS, JS, картинки). Файлы собираются в STATIC_ROOT при collectstatic.
STATIC_URL = 'static/'

# Куда перенаправлять после успешного входа и после выхода (встроенная авторизация Django).
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

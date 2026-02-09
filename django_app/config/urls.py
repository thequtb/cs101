"""
Маршрутизация URL: какой адрес ведёт на какую страницу (view).
path('путь/', view, name='имя') — имя используется в шаблонах: {% url 'имя' %}.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Главная: отображаем шаблон home.html (TemplateView).
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # Админ-панель Django.
    path('admin/', admin.site.urls),
    # Авторизация: /accounts/login/, /accounts/logout/ и др. (встроенное приложение auth).
    path('accounts/', include('django.contrib.auth.urls')),
    path('sample/', include('sample.urls')),
]

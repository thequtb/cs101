from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='sample_note_list'),
]

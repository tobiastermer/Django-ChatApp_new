# first_django_app/urls.py
from django.contrib import admin
from django.urls import path
from chat.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # Root-URL definiert
    path('chat/', index)
]

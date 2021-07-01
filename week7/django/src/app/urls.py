from django import urls
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'', views.home, name='home'),
    path('add_todo', views.add_todo)
]
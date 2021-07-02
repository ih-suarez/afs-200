from django import urls
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('add_todos', views.add_todo, name='add_me'),
    path('login', views.home, name='home'),
    # path('delete_todo/<int:id>', views.delete_todo, name='delete_me')
]
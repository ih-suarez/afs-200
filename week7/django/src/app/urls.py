from django import urls
# from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('add_todos', views.add_todo, name='add_me'),
    path('home', views.home, name='home'),
    path(r'delete_todo/<int:id>', views.delete_todo, name='delete_me')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo', views.add_todo, name='add_todo'),
    path(r'delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    
]
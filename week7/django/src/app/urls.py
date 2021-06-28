from django import urls
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', views.home, name='home'),
    url(r'add_todo/', views.add_todo),
    
]
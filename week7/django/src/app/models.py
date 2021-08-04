from django.db import models

# Create your models here.
class Todo(models.Model):
  todo = models.CharField(max_length=200, default='')
  added_date = models.CharField(max_length=10, default='')

  class User(models.Model):
    username = models.CharField(max_length=22, default='')
    password = models.CharField(max_length=33, default='')
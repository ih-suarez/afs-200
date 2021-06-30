from django.db import models

# Create your models here.
class Todo(models.Model):
  titel = models.CharField(max_length=20, default='Title')
  description = models.CharField(max_length=60, default='Todo')
  date_posted = models.CharField(max_length=15, default='')
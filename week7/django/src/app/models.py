from django.db import models

# Create your models here.
class Todo(models.Model):
  todo = models.CharField(max_length=200, default='')
  added_date = models.DateTimeField(auto_now=True, blank=True)
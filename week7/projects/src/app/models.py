from django.db import models
from datetime import datetime


class Todo(models.Model):
    todo = models.CharField(max_length=50, blank=True, default='')
    added_date = models.DateTimeField(datetime.now())
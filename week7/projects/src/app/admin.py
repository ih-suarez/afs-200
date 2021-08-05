from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'todo': ['todo', 'added_date']}),
    ]

admin.site.register(Todo)
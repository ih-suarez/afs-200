# Generated by Django 3.2.5 on 2021-07-08 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_todo_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 8, 1, 52, 54, 323376)),
        ),
    ]

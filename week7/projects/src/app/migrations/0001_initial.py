# Generated by Django 3.2.6 on 2021-08-05 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(blank=True, max_length=50)),
                ('added_date', models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 5, 21, 49, 40, 342409))),
            ],
        ),
    ]
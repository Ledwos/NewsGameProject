# Generated by Django 3.0.2 on 2020-03-03 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200210_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='points',
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-27 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0043_auto_20201227_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book',
            new_name='genre',
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-05 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20201203_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

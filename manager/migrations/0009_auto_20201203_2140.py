# Generated by Django 3.1.3 on 2020-12-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20201202_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
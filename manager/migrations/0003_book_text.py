# Generated by Django 3.1.3 on 2020-12-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_book_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(default='Hello'),
            preserve_default=False,
        ),
    ]
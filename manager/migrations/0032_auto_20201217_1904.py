# Generated by Django 3.1.3 on 2020-12-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0031_testcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcomment',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_title', to='manager.testtale'),
        ),
    ]

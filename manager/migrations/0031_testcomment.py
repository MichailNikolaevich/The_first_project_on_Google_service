# Generated by Django 3.1.3 on 2020-12-16 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0030_testtale'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.testtale')),
            ],
        ),
    ]

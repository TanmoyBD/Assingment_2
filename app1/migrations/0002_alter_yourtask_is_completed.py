# Generated by Django 4.2.3 on 2023-08-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourtask',
            name='is_completed',
            field=models.IntegerField(default=0),
        ),
    ]

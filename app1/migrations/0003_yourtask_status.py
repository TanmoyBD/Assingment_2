# Generated by Django 4.2.3 on 2023-08-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_yourtask_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='yourtask',
            name='status',
            field=models.CharField(default='Not Completed', max_length=20),
        ),
    ]

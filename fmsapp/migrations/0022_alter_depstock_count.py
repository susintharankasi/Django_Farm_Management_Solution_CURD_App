# Generated by Django 4.1.4 on 2023-04-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsapp', '0021_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depstock',
            name='count',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.1 on 2020-09-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
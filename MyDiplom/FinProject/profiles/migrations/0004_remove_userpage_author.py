# Generated by Django 5.0.1 on 2024-03-28 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userpage_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpage',
            name='author',
        ),
    ]

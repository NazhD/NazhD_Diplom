# Generated by Django 5.0.1 on 2024-03-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userpage_image'),
        ('warhammer', '0008_remove_imagefile_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpage',
            name='author',
            field=models.ManyToManyField(to='warhammer.imagefile'),
        ),
    ]

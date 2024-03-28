# Generated by Django 5.0.1 on 2024-03-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userpage_image'),
        ('warhammer', '0006_imagefile_author_alter_imagefile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagefile',
            name='author',
        ),
        migrations.AddField(
            model_name='imagefile',
            name='author',
            field=models.ManyToManyField(to='profiles.userpage'),
        ),
    ]

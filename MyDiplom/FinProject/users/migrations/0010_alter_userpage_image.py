# Generated by Django 5.0.1 on 2024-02-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_userpage_image_alter_userpage_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpage',
            name='image',
            field=models.ImageField(null=True, upload_to='users/images/'),
        ),
    ]

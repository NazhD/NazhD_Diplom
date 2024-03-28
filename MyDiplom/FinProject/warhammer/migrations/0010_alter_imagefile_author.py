# Generated by Django 5.0.1 on 2024-03-28 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userpage_author'),
        ('warhammer', '0009_imagefile_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.userpage'),
        ),
    ]
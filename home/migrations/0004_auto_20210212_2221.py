# Generated by Django 3.1.6 on 2021-02-12 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210212_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='social_url',
            new_name='url',
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-16 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210214_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactheader',
            name='email_address',
        ),
        migrations.AlterField(
            model_name='contactheader',
            name='promo_text',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]

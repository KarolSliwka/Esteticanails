# Generated by Django 3.1.6 on 2021-02-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logotype', models.ImageField(blank=True, null=True, upload_to='logotype/')),
            ],
            options={
                'verbose_name_plural': 'Logotype',
            },
        ),
    ]

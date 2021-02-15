# Generated by Django 3.1.6 on 2021-02-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210215_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Slide ', editable=False, max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/carousel/')),
                ('title', models.CharField(blank=True, max_length=124, null=True)),
                ('text', models.TextField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Slides',
        ),
    ]
# Generated by Django 2.2.1 on 2021-10-24 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20211024_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cover',
        ),
    ]

# Generated by Django 3.0 on 2021-09-05 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210825_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='escritorio',
        ),
    ]

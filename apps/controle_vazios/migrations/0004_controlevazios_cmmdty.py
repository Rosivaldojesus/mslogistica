# Generated by Django 3.0 on 2021-08-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_vazios', '0003_auto_20210814_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlevazios',
            name='cmmdty',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0 on 2021-08-24 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controle_vazios', '0008_auto_20210824_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlevazios',
            name='vendido_por_filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Vendido_Por_Filial', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.0 on 2021-08-24 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controle_vazios', '0006_auto_20210817_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlevazios',
            name='cadastrado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Cadastrado_Por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='controlevazios',
            name='vendido_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Vendido_Por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='controlevazios',
            name='vendido_por_filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Vendido_Por_Filial', to=settings.AUTH_USER_MODEL),
        ),
    ]

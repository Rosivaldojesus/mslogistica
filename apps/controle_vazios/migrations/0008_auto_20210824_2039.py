# Generated by Django 3.0 on 2021-08-24 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210824_2038'),
        ('controle_vazios', '0007_auto_20210824_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlevazios',
            name='vendido_por_filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Vendido_Por_Filial', to='core.Filial'),
        ),
    ]
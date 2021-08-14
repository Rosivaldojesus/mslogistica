# Generated by Django 3.0 on 2021-08-14 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControleFretes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pol', models.CharField(max_length=255)),
                ('pod', models.CharField(max_length=255)),
                ('carrier', models.CharField(max_length=255)),
                ('quotation', models.CharField(max_length=255)),
                ('cmmdty', models.CharField(max_length=255)),
                ('dv20', models.CharField(max_length=255)),
                ('dv40', models.CharField(max_length=255)),
                ('hc40h', models.CharField(max_length=255)),
                ('valid', models.DateField(blank=True, null=True)),
                ('detention', models.CharField(max_length=255)),
                ('demurrage', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'ControleFretes',
            },
        ),
    ]
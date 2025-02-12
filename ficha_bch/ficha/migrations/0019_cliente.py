# Generated by Django 5.1.5 on 2025-02-04 20:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0018_ejecutivos_oficina_oportunidad_sucursal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('rut', models.CharField(help_text='Formato: XXXXXXXX-X', max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='El RUT debe estar en formato XXXXXXXX-X', regex='^\\d{7,8}-[\\dkK]$')])),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=200)),
                ('tipo_producto', models.CharField(max_length=100)),
                ('tipo_cliente', models.CharField(max_length=40)),
            ],
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0020_remove_sucursal_cantidad_ejecutivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errores_agravantes',
            name='nota',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='errores_agravantes',
            name='puntaje',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='canal',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='username_ejecutivo',
            field=models.CharField(default='', max_length=20, verbose_name='Log Ejecutivo'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='cant_ejecutivo',
            field=models.CharField(default='', max_length=5, verbose_name='Cantidad Ejecutivos'),
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0030_rename_fitro_revision_filtro_revision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filtro_revision',
            old_name='nombre_ejecutivo',
            new_name='Ejec.Responsable',
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-22 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0005_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
    ]

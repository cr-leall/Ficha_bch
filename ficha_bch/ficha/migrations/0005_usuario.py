# Generated by Django 5.1.5 on 2025-01-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0004_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('ultimo_login', models.DateTimeField(auto_now=True)),
                ('esta_activa', models.BooleanField(default=True)),
                ('es_personal', models.BooleanField(default=False)),
                ('roles', models.CharField(choices=[('usuario', 'Analista de evaluación '), ('admin', 'Administrador')], default='usuario', max_length=7)),
            ],
        ),
    ]

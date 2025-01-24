from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Pilares (models.Model):
    formalidad = models.CharField(verbose_name="Formalidad", max_length=20)
    gest_otorgamiento = models.CharField(verbose_name="Gestión de Otorgamiento", max_length=20)
    depura_antecedent = models.CharField(verbose_name="Depuracion de Antecedentes", max_length=20)
    ingreso_datos = models.CharField(verbose_name="Ingreso de Datos", max_length=20)


class Usuario(models.Model):
    # Campos de texto
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField( max_length=30)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    # Campos de fechas
    ultimo_login = models.DateTimeField(auto_now=True)

    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Analista de evaluación '),
        ('admin', 'Supervisor'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')
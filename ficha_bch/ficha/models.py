from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    # Campos de texto
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    # Campos de fechas
    ultimo_login = models.DateTimeField(auto_now=True)

    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Analista de evaluación'),
        ('supervisor', 'Supervisor'),
    ]
    roles = models.CharField(max_length=10, choices=OPCIONES_ROL, default='usuario')

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username

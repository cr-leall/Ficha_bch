from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class Pilares(models.Model):
    id_pilar = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Parametro(models.Model):
    id_parametro = models.AutoField(primary_key=True)
    nombre_parametro = models.CharField(max_length=150)

class Errores_agravantes(models.Model):
    id_base = models.AutoField(primary_key=True)
    nombre_parametro = models.CharField(max_length=150)
    tipo_error = models.CharField(max_length=150)
    tipo_cliente = models.CharField(max_length=80) 


def validar_rut(rut):
    rut = rut.replace(".", "").replace("-","").upper()
    cuerpo = rut[:-1]
    dv = rut[-1]

    if not cuerpo.isdigit():
        raise ValidationError("Solo se adminten caracteres numericos")

    suma = 0
    multiplicador = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    dv_calculado = str(11 - resto) if resto != 0 else "0"
    if dv_calculado =="10":
        dv_calculado = "K"

    if dv != dv_calculado:
                raise ValidationError("El digito verificador del RUT no es válido")
class cliente(models.Model):
    rut = models.CharField(
        primary_key=True,
        max_length=10,
        validators=[
             RegexValidator(
                regex = r'^\d{7,8}-[\dkK]$',
                  message = "El RUT debe estar en formato XXXXXXXX-X"
                        )
                    ],
                    help_text="Formato: XXXXXXXX-X"
                        )
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField(unique=True)
    tipo_producto = models.CharField(max_length=100)

    def clean(self):
        super().clean()
        self.rut = self.rut.replace(".","").upper()
        validar_rut(self.rut)
    def __str__(self):
         return f"{self.rut} - {self.nombre}"
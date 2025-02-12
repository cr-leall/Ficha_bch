from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='static/img', default='default.jpg')
    def __str__(self):
        return self.user.username

class Pilares(models.Model):
    id_pilar = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Parametro(models.Model):
    id_parametro = models.AutoField(primary_key=True)
    nombre_parametro = models.CharField(max_length=150)

class Errores_agravante(models.Model):
    id_base = models.AutoField(primary_key=True)
    nombre_parametro = models.CharField(max_length=100)
    tipo_error = models.CharField(max_length=100)
    tipo_cliente = models.CharField(max_length=20)
    nota = models.CharField(max_length=20,default="") 
    puntaje = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
         return self.nombre_parametro


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
    tipo_producto = models.CharField(max_length=100)
    tipo_cliente = models.CharField(max_length=40)

    def clean(self):
        super().clean()
        self.rut = self.rut.replace(".","").upper()
        validar_rut(self.rut)
    def __str__(self):
         return f"{self.nombre} {self.apellido}"

def val_rut_ejecutivo(rut_ejecutivo):
    rut_ejecutivo = rut_ejecutivo.replace(".", "").replace("-","").upper()
    cuerpo = rut_ejecutivo[:-1]
    dv = rut_ejecutivo[-1]

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
class ejecutivo(models.Model):
    rut_ejecutivo = models.CharField(
         primary_key=True,
         max_length=10,
         validators=[
             RegexValidator(
                regex = r'^\d{7,8}-[\dkK]$',
                  message = "El RUT debe estar en formato XXXXXXXX-X"
                        )
                    ],
                    help_text="Formato: 20222777-X"
                        )
    nombre_ejecutivo = models.CharField(max_length=100)
    username_ejecutivo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_ejecutivo} / Username: {self.username_ejecutivo}"

class oficina(models.Model):
    cui = models.CharField(("CUI"),primary_key=True, max_length=10)
    nombre_ofi = models.CharField(("Nombre Oficina"),max_length=50)  

    def __str__(self):
        return self.nombre_ofi
class sucursal(models.Model):
    cod_sucursal = models.CharField(("Codigo Sucursal"),primary_key=True, max_length=10)
    nombre_suc = models.CharField(("Nombre Sucursal"),max_length=50)
    aprobador = models.CharField(("Nombre aprobador"),max_length=30)
    n_oportunidad = models.CharField(("N° Oportunidad"),max_length=100)
    cant_ejecutivo = models.CharField(("Cantidad Ejecutivos"),max_length=5,default="")

    def __str__(self):
         return self.nombre_suc
class oportunidad(models.Model):
    id_oportunidad = models.AutoField(primary_key=True)
    username_ejecutivo = models.CharField(("Log Ejecutivo"),default="",max_length=20)
    cui = models.ForeignKey(oficina, on_delete=models.CASCADE, default=0)
    inconsistencia = models.CharField(max_length=200)
    monto_solicitado = models.IntegerField(("monto solicitado"), default=0)
    proceso_credito = models.CharField(max_length=20)
    pauta_evaluacion = models.CharField(max_length=30)
    desicion_final = models.BooleanField
    anio_mes = models.DateField("Fecha", auto_now=False, auto_now_add=False, default=date.today)
    canal = models.CharField(max_length=5, default="")
    prod_eval = models.CharField(("producto evaluado"),max_length=50) 

class filtro_revision(models.Model):
    id_filtro = models.AutoField(primary_key=True)
    cui = models.ForeignKey(oficina, on_delete=models.CASCADE)
    rut = models.ForeignKey(cliente, on_delete=models.CASCADE) 
    nombre_ejecutivo = models.CharField(ejecutivo,('Ejec.Responsable'), max_length=40)
    username_ejecutivo = models.CharField(ejecutivo, max_length=20)
    tipo_cliente = models.CharField(cliente, max_length=10)
    nombre_suc = models.CharField(sucursal, max_length=40)
    tipo_producto = models.CharField(cliente, max_length=20)
    monto_solicitado = models.IntegerField(("monto solicitado"), default=0)
    rut = models.CharField(cliente, max_length=10)
    num_revision= models.CharField(('Revisión N°: '),max_length=10)
    
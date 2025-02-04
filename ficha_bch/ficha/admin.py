from django.contrib import admin
from .models import Pilares, cliente, Errores_agravantes,Parametro
# Register your models here.
admin.site.register(Pilares)
admin.site.register(cliente)
admin.site.register(Errores_agravantes)
admin.site.register(Parametro)
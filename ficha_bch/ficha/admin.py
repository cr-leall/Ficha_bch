from django.contrib import admin
from .models import Pilares,Errores_agravantes,Parametro,cliente,ejecutivos,sucursal,oficina,oportunidad
# Register your models here.
admin.site.register(Pilares)
admin.site.register(cliente)
admin.site.register(Errores_agravantes)
admin.site.register(Parametro)
admin.site.register(ejecutivos)
admin.site.register(sucursal)
admin.site.register(oficina)
admin.site.register(oportunidad)
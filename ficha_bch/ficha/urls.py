from django.contrib import admin
from django.urls import path, include
from .views import login,index,base,registro,gestion_otorga,depuracion_antece,ingreso_datos

urlpatterns = [
    path('',login,name='LOGIN'),
    path('registro/',registro,name='REGIS'),
    path('base/',base,name='BASE'),
    path('index/',index,name='INDEX'),
    path('gestion_otorga/',gestion_otorga,name='GESTION'),
    path('depuracion_antece/',depuracion_antece,name='DEPURACION'),
    path('ingreso_datos/',ingreso_datos,name='INGRESOS'),
]
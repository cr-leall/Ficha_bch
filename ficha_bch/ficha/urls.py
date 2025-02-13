from django.contrib import admin
from django.urls import path, include
from .views import login, base, registro, gestion_otorga, depuracion_antece, ingreso_datos, index

urlpatterns = [
    path('', login, name='login'),
    path('registro/', registro, name='registro'),
    path('base/', base, name='base'),
    path('index/', index, name='index'),
    path('gestion_otorga/', gestion_otorga, name='gestion'),
    path('depuracion_antece/', depuracion_antece, name='depuracion'),
    path('ingreso_datos/', ingreso_datos, name='ingresos'),
]
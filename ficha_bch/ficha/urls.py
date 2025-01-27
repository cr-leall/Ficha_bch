from django.contrib import admin
from django.urls import path, include
from .views import login,index,base,registro,ficha

urlpatterns = [
    path('',login,name='LOGIN'),
    path('registro/',registro,name='REGIS'),
    path('base/',base,name='BASE'),
    path('index/',index,name='INDEX'),
    path('ficha/',ficha,name='FICHA'),
]
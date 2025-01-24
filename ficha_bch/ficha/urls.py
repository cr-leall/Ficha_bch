from django.contrib import admin
from django.urls import path, include
from .views import login,index,base,registro

urlpatterns = [
    path('',login,name='LOGIN'),
    path('base/',base,name='BASE'),
    path('index/',index,name='INDEX'),
    path('registro/',registro,name='REGIS'),

]
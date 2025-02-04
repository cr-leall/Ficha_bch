from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_aut
#from django.db import IntegrityError
#from django.utils import timezone
#from django.contrib.auth.decorators import login_required
# Create your views here.
def registro(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        roles = request.POST['roles']
        try:
            u = User.objects.create_user(username=username, email=email, password=password)
            mensaje="Usuario Existente"
            return render(request, 'web/registro.html', {'msg': mensaje})
            
        except:
            u = User()
            u.first_name = nombres
            u.last_name = apellidos 
            u.email = email
            u.username = username
            u.password = password
            u.roles = roles
            u.save()
            mensaje="Registro Completa con exito"
            us = authenticate(request, username=username, password=password)
            login_aut(request, us)
        return redirect('/index', {'user' : us})  # Redirigir a la vista deseada
    return render(request, 'web/registro.html')

def login(request):
    return render(request,'web/login.html')

def base(request):
    return render(request,'web/base.html')

def index(request):
    return render(request,'web/index.html')

def gestion_otorga(request):
    return render(request,'web/gestion_otorga.html')

def depuracion_antece(request):
    return render(request,'web/depuracion_antece.html')

def ingreso_datos(request):
    return render(request,'web/ingreso_datos.html')



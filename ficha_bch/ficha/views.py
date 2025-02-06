from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_aut
from django.http import JsonResponse
from .models import cliente, ejecutivos, oficina, sucursal, oportunidad

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
            mensaje = "Usuario Existente"
            return render(request, 'web/registro.html', {'msg': mensaje})
        except:
            u = User()
            u.first_name = nombres
            u.last_name = apellidos
            u.email = email
            u.username = username
            u.set_password(password)  # Usar set_password para guardar la contraseña de manera segura
            u.save()
            mensaje = "Registro Completo con éxito"
            us = authenticate(request, username=username, password=password)
            login_aut(request, us)
        return redirect('/index', {'user': us})  # Redirigir a la vista deseada
    
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

# Otras vistas...

def get_data(request):
    codigo_oficina = request.GET('codigo_oficina')
    rut = request.GET('rut')

    try:
        cliente_data = cliente.objects.get(rut=rut)
        oficina_data = oficina.objects.get(cui=codigo_oficina)
        # Aquí puedes obtener más datos según tus necesidades

        data = {
            'success': True,
            'ejec_responsable': cliente_data.nombre,
            'login_creador': cliente_data.email,
            'tipo_cliente': cliente_data.tipo_cliente,
            'sucursal': oficina_data.nombre_ofi,
            'producto': cliente_data.tipo_producto,
            'm_solicitado': '1000',  # Ejemplo de dato
            'rut_modificar': cliente_data.rut,
            'revision_numero': '1'  # Ejemplo de dato
        }
    except cliente.DoesNotExist:
        data = {'success': False, 'message': 'Cliente no encontrado'}
    except oficina.DoesNotExist:
        data = {'success': False, 'message': 'Oficina no encontrada'}

    return JsonResponse(data)

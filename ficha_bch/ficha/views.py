from django.shortcuts import render
from .models import cliente, ejecutivo, oficina, sucursal, oportunidad
#Import Modelo de tablas User
from django.contrib.auth.models import User
from .models import UserProfile
# Import Libreria de autentificacion
from django.contrib.auth import authenticate, logout,login as login_auth
#Import decorators para impedir ingreso de paginas sin estar registrado
from django.contrib.auth.decorators import login_required,permission_required
from django.http import JsonResponse
from django.db import IntegrityError
# Create your views here.

def registro(request):
    if request.method == 'POST':
        nombres = request.POST.get("nombres").strip()
        apellidos = request.POST.get("apellidos").strip()
        email = request.POST.get("email").strip()
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()
        password2 = request.POST.get("password2").strip()
        roles = request.POST.get("roles").strip()

        # Validar que el correo no esté en uso
        if User.objects.filter(email=email).exists():
            message = "El correo ya está en uso"
            return render(request, 'web/registro.html', {'Error': message})

        try:
            # Intentar crear un nuevo usuario
            u = User.objects.create_user(username=username, email=email, password=password)
            u.first_name = nombres
            u.last_name = apellidos
            u.save()

            # Crear el perfil de usuario
            perfil = UserProfile(user=u, roles=roles)
            perfil.save()

            mensaje = "Registro exitoso"

            # Autenticar y loguear al usuario
            us = authenticate(request, username=username, password=password)
            login_auth(request, us)

            return render(request, 'web/login.html', {'user': us, 'msg': mensaje})
        except IntegrityError:
            # Si el usuario ya existe, manejar la excepción y mostrar el mensaje de error
            mensaje = "Usuario existente"
            return render(request, 'web/registro.html', {'msg': mensaje})

    # Renderizar la página de registro si el método no es POST
    return render(request, 'web/registro.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        # Validar que los campos no estén vacíos o contengan solo espacios en blanco
        if not username or not password:
            message = "Usuario y contraseña son obligatorios y no deben contener solo espacios en blanco."
            return render(request, 'web/login.html', {'error': message})
        # Autenticar al usuario
        us = authenticate(request, username=username, password=password)
        if us is not None and us.is_active:
            login_auth(request, us)
            message = "Bienvenido a FichaBch Buen Día " + us.first_name
            return render(request, 'web/index.html', {'user': us, 'success': message})
        else:
            message = "Usuario o contraseña incorrectos"
            return render(request, 'web/login.html', {'error': message})
    return render(request, 'web/login.html')

def logout_view(request):
	logout(request)
	message = "Cerraste sesion correctamente"
	return render(request,'web/login.html',{'output':message})

def base(request):
    clientes_con_credito = []
    oficina_data = {}
    if request.method == 'POST':
        cod_oficina = request.POST.get("cod_oficina", "").strip()
        rut_cliente = request.POST.get("rut_cliente", "").strip()

        # Validar que el código de oficina no esté vacío
        if cod_oficina:
            # Obtener datos de la oficina
            oficina_data = oportunidad.objects.filter(cui=cod_oficina).values(
                'cliente__rut', 'cliente__nombre', 'ejecutivos__nombre_ejecutivo', 'username_ejecutivo', 
                'cliente__tipo_cliente', 'sucursal__nombre_suc', 'prod_eval', 'monto_solicitado', 'revision_numero'
            ).first()

            # Filtrar clientes por RUT si se proporciona
            if rut_cliente:
                clientes_con_credito = cliente.objects.filter(
                    oportunidad__cui=cod_oficina,
                    rut=rut_cliente
                ).distinct()
            else:
                clientes_con_credito = cliente.objects.filter(
                    oportunidad__cui=cod_oficina
                ).distinct()

    return render(request, 'web/base.html', {
        'clientes_con_credito': clientes_con_credito,
        'oficina_data': oficina_data
    })

def index(request):
    return render(request,'web/index.html')

def gestion_otorga(request):
    return render(request,'web/gestion_otorga.html')

def depuracion_antece(request):
    return render(request,'web/depuracion_antece.html')

def ingreso_datos(request):
    return render(request,'web/ingreso_datos.html')

# Otras vistas...

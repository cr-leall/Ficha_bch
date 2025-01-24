from django.shortcuts import render
from .form import UsuarioForm

# Create your views here.
def login(request):
    return render(request,'web/login.html')

def base(request):
    return render(request,'web/base.html')

def index(request):
    return render(request,'web/index.html')


def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request,'web/registro.html')
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def tienda(request):
    return render(request, 'tienda.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def ubicacion(request):
    return render(request, 'ubicacion.html')

def repuestos(request):
    return render(request, 'repuestos.html')

def cuerda(request):
    return render(request, 'cuerda.html')

def percusion(request):
    return render(request, 'percusion.html')

def amplificadores(request):
    return render(request, 'amplificadores.html')

def registro(request):
    return render(request, 'registro.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

def carrito(request):
    return render(request, 'carrito.html')
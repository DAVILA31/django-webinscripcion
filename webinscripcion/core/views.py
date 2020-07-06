from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def mision (request):
    return render(request, 'core/misionyvision.html')

def direccion(request):
    return render(request, 'core/direccion.html')

def aviso(request):
    return render(request, 'core/aviso.html')


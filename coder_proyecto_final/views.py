from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def pag_principal(request): 
    return render(request, "index.html")

def crear_remera(request):
    return render(request, "remera_formulario.html")

def crear_buzo(request):
    return render(request, "buzo_formulario.html")

def crear_pantalon(request):
    return render(request, "pantalon_formulario.html")

def buscar_buzo(request):
    return render(request, "buscar_buzo.html")

def buscar(request):
    respuesta = f"estoy buscando el buzo :  {request.GET['nombre']}" 
    
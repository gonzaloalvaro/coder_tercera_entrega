from django.shortcuts import render
from stock.models import buzos,remeras,pantalones
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def crear_pantalon(request):
    if request.method == "POST" :
        nuevo_pantalon = pantalones(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            talle = request.POST["talle"],
            cantidad_en_stock = request.POST["cantidad en stock"],
        )
        nuevo_pantalon.save()
        return render(request, "index.html")
    return render(request, "pantalon_formulario.html")

def crear_remera(request):
    if request.method == "POST" :
        nueva_remera = remeras(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            talle = request.POST["talle"],
            cantidad_en_stock = request.POST["cantidad en stock"],
        )
        nueva_remera.save()
        return render(request, "index.html")

    return render(request, "remera_formulario.html")

def crear_buzo(request):
    if request.method == "POST" :
        nuevo_buzo = buzos(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            talle = request.POST["talle"],
            cantidad_en_stock = request.POST["cantidad en stock"]
        )
        nuevo_buzo.save()
        return render(request, "index.html")
    return render(request, "buzo_formulario.html")
    
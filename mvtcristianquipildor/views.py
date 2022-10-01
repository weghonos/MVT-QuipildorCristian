from usuarios.models import Usuario
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

def crear_usuarios(request):
    usuario1 = Usuario(nombre="Eduardo",apellido="Rivera",edad=50,fecha=datetime.now())
    usuario2 = Usuario(nombre="Yamila",apellido="Rivera",edad=34,fecha=datetime.now())
    usuario3 = Usuario(nombre="Juan",apellido="Carrizo",edad=74,fecha=datetime.now())
    usuario1.save()
    usuario2.save()
    usuario3.save()

    template = loader.get_template("crea_usuarios.html")
    template_renderizado = template.render({})

    return HttpResponse(template_renderizado)

def ver_usuarios(request):
    personas = Usuario.objects.all()

    template = loader.get_template("ver_usuarios.html")
    template_renderizado = template.render({"personas": personas})

    return HttpResponse(template_renderizado)
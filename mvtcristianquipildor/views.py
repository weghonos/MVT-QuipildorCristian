from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader

def hola(request):
    return HttpResponse("hola")

def fecha(request, persona):
    template = loader.get_template("template.html")
    template_renderizado = template.render({"persona" : persona})
    
    return HttpResponse(template_renderizado)
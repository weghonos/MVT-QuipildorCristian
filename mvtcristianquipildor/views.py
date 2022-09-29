from django.http import HttpResponse
from datetime import datetime
def hola(request):
    return HttpResponse("hola")

def fecha(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"La fecha actual es {fecha_hora}")
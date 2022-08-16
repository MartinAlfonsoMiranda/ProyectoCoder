from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

# Create your views here.
from django.template import loader


def curso(request, nombre, camada):
    cur = Curso(nombre=nombre, camada=camada)
    cur.save()

    plantilla = loader.get_template("template.html")

    context = {
        "nombre": cur.nombre,
        "camada": cur.camada,
    }
    documento = plantilla.render(context)
    return HttpResponse(documento)
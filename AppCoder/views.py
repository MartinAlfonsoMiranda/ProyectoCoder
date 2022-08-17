from django.http import HttpResponse
from django.template import loader
from AppCoder.models import familiar

# Create your views here.
from django.template import loader


def crear_familiares(request):
    familiar1 = familiar(nombre='Rosana', apellido='Pierrone', fecha_nacimiento="1973-10-27", dni=23607104)
    familiar2 = familiar(nombre='Javier', apellido='Miranda', fecha_nacimiento="1969-05-30", dni=20142945)
    familiar3 = familiar(nombre='Julieta', apellido='Miranda', fecha_nacimiento="2002-06-24", dni=43648232)

    familiar3.save()
    familiar2.save()
    familiar1.save()

    context = {
        'information': {
            'Madre': familiar1,
            'Padre': familiar2,
            'Hermana': familiar3
        }
    }
    plantilla = loader.get_template('template.html')
    documento_texto = plantilla.render(context)

    return HttpResponse(documento_texto)

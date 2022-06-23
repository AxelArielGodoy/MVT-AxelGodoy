from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Template, Context
from .models import Prueba
from datetime import datetime
# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Mi perro dinamita</h1>')

def un_template(request):
    
    template = loader.get_template('index.html')
    
    prueba1 = Prueba(nombre = 'Azucena',numero = 55,fecha ='1960-12-02')
    prueba2 = Prueba(nombre = 'Carlos', numero = 60,fecha ='1950-05-05')
    prueba3 = Prueba(nombre = 'Yamila', numero = 30,fecha ='2000-09-11')
    # prueba4 = Prueba(numero = 55)
    # prueba5 = Prueba(fecha = 22/22/22)
    # fecha = datetime.date(22/22/22)
    prueba1.save()
    prueba2.save()
    prueba3.save()
    # prueba4.save()
    # prueba5.save()
    
    Prueba.objects.all()
    
    
    documento = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    return HttpResponse(documento)
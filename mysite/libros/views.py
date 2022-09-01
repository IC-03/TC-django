from django.shortcuts import render #genera la pag

# Create your views here.
#imports
from django.template import loader
from django.http import HttpResponse


def index(request): #configurado para get
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {} #info de la lógica
    #respuesta
    return HttpResponse(template.render(context,request))
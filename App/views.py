from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
import datetime

from django.template import Template, Context, loader



# Create your views here.
def familiares(self):
    fam1 = Familiar(nombre = 'Vilma', edad = 57, vinculo = 'mamá', nacimiento = '1965-02-01')
    fam2 = Familiar(nombre = 'Maite', edad = 24, vinculo = 'hermana', nacimiento = '1997-11-25')
    fam3 = Familiar(nombre = 'Horacio', edad = 57, vinculo = 'papá', nacimiento = '1965-04-12')

    fam1.save()
    fam2.save()
    fam3.save()
    
    dic = {"fam1": fam1, "fam2":fam2, "fam3":fam3}

    plantilla = loader.get_template("plantilla1.html")
    doc = plantilla.render(dic)    
 

    return HttpResponse(doc)


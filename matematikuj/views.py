from django.shortcuts import render, HttpResponse, loader
from django.views.generic.list import ListView
from django.db import models
from .models import Menu_bloky, Pocetni_priklady, Tema
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Rocnik = ["6.ročník","7.ročník","8.ročník","9.ročník"]
def index(request):
    return render(request,"matematikuj/index.html", dict(bloky = Menu_bloky.objects.all(), homepage = True))

def studnice(request):
    return render(request,"matematikuj/index.html", dict(bloky = Menu_bloky.objects.all(), studnice = True))

def temata(request):
    temataSS = []
    temataZS = []
    soubor = open(BASE_DIR + '/matematikuj/static/pocet_uloh.txt',"r")
    temata = Tema.objects.all()
    for tema in temata:
        if len(tema.podtema) == 0:
            nikam = soubor.readline()
            tema.pocet_uloh = soubor.readline()
            if tema.skola == '1':
                temataZS.append(tema)
            else:
                temataSS.append(tema)
    soubor.close()
    return render(request,"matematikuj/index.html", dict(bloky = Menu_bloky.objects.all(), 
                temata_SS = temataSS, 
                temata_ZS = temataZS))
    
def podtemata(request, tema):
    podtemata_splnujici_tema = []
    temata = Tema.objects.all()

    for tm in temata:
        if ((tm.tema == tema) and (len(tm.podtema) != 0) and (len(tm.kapitola) ==0)):
            podtemata_splnujici_tema.append(tm)
    return render(request,"matematikuj/index.html", dict(bloky = Menu_bloky.objects.all(), podtemata_SS = podtemata_splnujici_tema, tema = tema))    

def priklady(request, tema, podtema):
    url = "matematikuj/index.html"
    priklady = Pocetni_priklady.objects.all()
    temata = Tema.objects.all()

    priklady_splnujici_tema = []
    kapitoly_splnujici_tema = []

    for tm in temata:
        if ((tm.tema == tema) and (tm.podtema==podtema)):
            if (len(tm.kapitola) !=0):
                kapitoly_splnujici_tema.append(tm)
                print(tm)
            else: 
                tema_bez_kapitoly = tm
    iterace = 1
    for priklad in priklady:
        if ((priklad.tema.tema == tema) and (priklad.tema.podtema == podtema)):
            priklad.ident = iterace
            iterace +=1
            if request.method == "POST":
                if request.POST.get(str(priklad.ident)):
                    priklad.ukaz_reseni = not(priklad.ukaz_reseni)

            priklady_splnujici_tema.append(priklad)   
    return render(request, url , dict(bloky = Menu_bloky.objects.all(), 
                priklady = priklady_splnujici_tema, 
                tema = tema, 
                podtema = podtema,
                kapitoly = kapitoly_splnujici_tema,
                tema_bez_kapitoly = tema_bez_kapitoly))

def pocet_uloh(request):
    if not request.user.is_staff:
        return HttpResponse("Zde není co hledat!")
    else:
        zapis = "<table>"
        soubor = open(BASE_DIR + '/matematikuj/static/pocet_uloh.txt',"w")
        pocet = 0
        for tema in Tema.objects.all():
            if len(tema.podtema) == 0: 
                for priklad in Pocetni_priklady.objects.all():
                    print(priklad.tema)
                    if priklad.tema.tema == tema.tema:
                        pocet += 1
                zapis = zapis + '<tr><td>' + tema.tema + '</td><td>' + str(pocet) + '</td></tr>'
                soubor.write(tema.tema + '\n')
                soubor.write(str(pocet) + '\n')
                pocet = 0
        zapis = zapis + '</table>'
        soubor.close()
        return HttpResponse(zapis)

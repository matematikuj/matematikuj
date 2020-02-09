from django.shortcuts import render, HttpResponse, loader
from django.views.generic.list import ListView
from django.db import models
from .models import Menu_bloky, Pocetni_priklady, Tema, Tema_ZS

Rocnik = ["6.ročník","7.ročník","8.ročník","9.ročník"]
def index(request):
    return render(request,"matematikuj/index.html", dict(bloky = Menu_bloky.objects.all(), homepage = True))

def temata(request):
    temataSS = []

    temata = Tema.objects.all()
    for tema in temata:
        if len(tema.podtema) == 0:
            temataSS.append(tema)
    print(Rocnik)

    return render(request,"matematikuj/index.html", dict(bloky = Menu_bloky.objects.all(), temata_SS = temataSS, Rocniky = Rocnik))
    
def priklady(request, tema):
    url = "matematikuj/index.html"
    priklady = Pocetni_priklady.objects.all()
    priklady_splnujici_tema = []

    iterace = 1
    for priklad in priklady:
        if priklad.tema.tema == tema:
            priklad.ident = iterace
            iterace +=1
            if request.method == "POST":
                if request.POST.get(str(priklad.ident)):
                    priklad.ukaz_reseni = not(priklad.ukaz_reseni)

            priklady_splnujici_tema.append(priklad)   
    return render(request, url , dict(bloky = Menu_bloky.objects.all(), priklady = priklady_splnujici_tema, tema = tema))

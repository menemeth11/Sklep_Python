from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from .views import *


def index(request):
    kategorie = Kategorie.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategorie_user = Kategorie.objects.get(pk=id)
    kategorie_produkt = Produkty.objects.filter(kategoria=kategorie_user)
    kategorie = Kategorie.objects.all()
    dane = {'kategorie_user': kategorie_user,
            'kategorie_produkt': kategorie_produkt,
            'kategorie': kategorie}
    return render(request, 'kategorie_produkt.html', dane)


def produkty(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategorie.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)

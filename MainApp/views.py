from django.shortcuts import render
from MainApp.models import Country, Language


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countries = Country.objects.all()

    context = {
        'countries': countries,
        'letters': letters
    }
    return render(request, 'countries-list.html', context)

def country_page(request, country):
    item = Country.objects.get(name=country)
    languages = item.languages.all()
    context = {
        'country': item.name,
        'languages': languages
    }
    return render(request, 'country-page.html', context)


def languages_list(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'languages.html', context)

def language_page(request, language):
    item = Language.objects.get(name=language)
    countries = item.country_set.all()
    context = {
        'language': item.name,
        'countries': countries
    }
    return render(request, 'language-page.html', context)

def countries_letter(request, letter):
    countries = Country.objects.filter(name__startswith=letter)

    context = {
        'letter': letter,
        'countries': countries,
    }
    return render(request, 'countries-letter.html', context)
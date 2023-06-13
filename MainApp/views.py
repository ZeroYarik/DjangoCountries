from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json
from itertools import chain

with open('country-by-languages.json') as f:
    countries = json.load(f)

with open('country-by-languages.json') as f:
    language = json.load(f)

def home(request):
    return render(request, 'index.html')

def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def country_page(request, country):
    for item in countries:
        if item['country'] == country:
            context = {'country': country,
                       'languages': item['languages']}
            return render(request, 'country-page.html', context)


def languages_list(request):
    languages = set()
    for item in countries:
        for language in item['languages']:
            languages.add(language)
    context = {'languages': languages}
    return render(request, 'languages.html', context)





    # text = "<ol>"
    # for certain_country in countries:
    #     text += f"<li><a href='/certain_country/{certain_country['country']}'>{certain_country['country']}</a></li>"
    # text += "</ol>"
    # return HttpResponse(text)
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

with open('country-by-languages.json') as f:
    file = f.read()
    countries = json.loads(file)

def home(request):
    return render(request, 'index.html')

def countries_list(request):
    text = "<ol>"
    for certain_country in countries:
        text += f"<li><a href='/certain_country/{certain_country['country']}'>{certain_country['country']}</a></li>"
    text += "</ol>"
    return HttpResponse(text)

def country_page(request, country):
    for certain_country in countries:
        if certain_country ['country'] == country:
            text = f"""<h2>{certain_country['country']}</h2>
            Languages: {certain_country['languages']}
            """
            return HttpResponse(text)
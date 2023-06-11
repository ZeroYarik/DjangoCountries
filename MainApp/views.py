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
        text += f"<li>{certain_country['country']}</li>"
    text += "</ol>"
    return HttpResponse(text)
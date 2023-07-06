from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('countries-list/', views.countries_list, name="countries"),
    path('countries/letter/<country>/', views.country_page, name='country-name'),
    path('countries/<letter>/', views.countries_list, name='countries-letter'),
    path('languages/', views.languages_list, name="languages"),
    path('language/<language>/', views.language_page, name="language"),
    # path('country/<letter>/', views.country_by_letter, name="cbl"),
]

from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('countries-list/', views.countries_list, name="countries"),
    path('country/<country>/', views.country_page, name="country"),
    path('languages/', views.languages_list, name="languages"),
    path('language/<language>/', views.language_page, name="language"),

]

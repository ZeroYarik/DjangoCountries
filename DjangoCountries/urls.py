from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list),
    path('certain_country/<country>/', views.country_page),


]

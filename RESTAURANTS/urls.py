#from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'RESTAURANTS'
urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('details/<int:resto_id>/', views.details, name='details'),
    path('search/', views.recherche, name='recherche'),
]

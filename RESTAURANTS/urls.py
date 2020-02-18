from django.conf.urls import url, include
from . import views

app_name = 'RESTAURANTS'
urlpatterns = [
    url(r'', views.restaurants, name='restaurants'),
]

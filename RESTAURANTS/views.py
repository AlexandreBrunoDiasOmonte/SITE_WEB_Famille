from django.shortcuts import render


# Create your views here.

def restaurants(request):
    return render(request, 'RESTAURANTS/restaurants.html')

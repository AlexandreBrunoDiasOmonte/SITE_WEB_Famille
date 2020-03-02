from django.shortcuts import render
from .models import Restaurant


def restaurants(request):
    restos = Restaurant.objects.filter(available=True)
   # liste = "\n".join(formated_restos)
    context = {'restos': restos}
    return render(request, 'RESTAURANTS/restaurants.html', context)

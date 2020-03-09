from django.shortcuts import render
from RESTAURANTS.models import Restaurant
from django.core.paginator import Paginator


def accueil(request):
    restos = Restaurant.objects.filter(available=True).order_by('name')
    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'RESTAURANTS/restaurants.html', context)

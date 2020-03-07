from django.shortcuts import render
from .models import Restaurant
from django.core.paginator import Paginator


def restaurants(request):
    restos = Restaurant.objects.filter(available=True)
    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'RESTAURANTS/restaurants.html', context)


def details(request, resto_id):
    resto = Restaurant.objects.get(pk=resto_id)
    context = {'resto': resto}
    return render(request, 'RESTAURANTS/details.html', context)


def recherche(request):
    query = request.GET.get('query')
    if not query:
        restos = Restaurant.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        restos = Restaurant.objects.filter(name__icontains=query)
    if not restos.exists():
        restos = Restaurant.objects.filter(ville__icontains=query)
    title = "Résultats pour la requête < %s >" % query

    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': title
    }
    return render(request, 'RESTAURANTS/recherche.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from django.core.paginator import Paginator


def restaurants(request):
    restos = Restaurant.objects.filter(available=True).order_by('name')
    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'RESTAURANTS/restaurants.html', context)


def details(request, resto_id):
    resto = get_object_or_404(Restaurant, pk=resto_id)
    context = {'resto': resto}
    return render(request, 'RESTAURANTS/details.html', context)


def recherche(request):
    query = request.GET.get('query')
    if not query:
        restos = Restaurant.objects.all().order_by('name')
    else:
        # title contains the query is and query is not sensitive to case.
        restos = Restaurant.objects.filter(name__icontains=query).order_by('name')
    if not restos.exists():
        restos = Restaurant.objects.filter(ville__icontains=query).order_by('name')
    if not restos.exists():
        restos = Restaurant.objects.filter(codePostal__icontains=query).order_by('name')
    results = "Résultats pour la requête < %s >" % query

    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'results': results
    }
    return render(request, 'RESTAURANTS/recherche.html', context)

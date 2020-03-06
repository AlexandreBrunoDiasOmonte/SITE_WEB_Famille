from django.shortcuts import render
from .models import Restaurant


def restaurants(request):
    restos = Restaurant.objects.filter(available=True)[:]
    context = {'restos': restos}
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
    context = {
        'restos': restos,
        'title': title
    }
    return render(request, 'RESTAURANTS/recherche.html', context)

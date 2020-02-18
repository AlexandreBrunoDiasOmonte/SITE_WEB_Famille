from django.shortcuts import render


def accueil(request):
    return render(request, 'Famille_DO/accueil.html')

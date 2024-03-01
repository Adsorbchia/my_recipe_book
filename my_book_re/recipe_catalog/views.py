from django.shortcuts import render

from recipe_catalog.models import Recipe


def catalog(request):
    goods = Recipe.objects.all()
    context = {
        'title': 'Cooking at home - все рецепты ',
        'goods': goods, 
        }
    return render(request, 'recipe_catalog/catalog.html', context)

def recipe(request):
    return render()

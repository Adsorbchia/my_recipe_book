from django.core.paginator import Paginator
from django.shortcuts import render
from recipe_catalog.models import Category, Recipe


def index(request):
    categories = Category.objects.all()
  
    recipes = Recipe.objects.filter(cooking_time__lt=35).filter(category__name='Завтраки').all()
    
   

    context = {
     'title': 'COOKING at HOME - Главная',
     'content': 'COOKING at HOME - книга полезных рецептов',
     'categories': categories,
     'recipes': recipes}
    return render(request, 'main/index.html', context)

def about(request):
    context = {'title': 'COOKING at HOME - О нас'}
    return render(request, 'main/about.html', context)



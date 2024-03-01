from django.shortcuts import render
from recipe_catalog.models import Category, Recipe


def index(request):
    categories = Category.objects.all()
    goods = Recipe.objects.filter(category__slug='zavtraki')|Recipe.objects.filter(id__lt=7)

    context = {
     'title': 'COOKING at HOME - Главная',
     'content': 'COOKING at HOME - книга полезных рецептов',
     'categories': categories,
     'goods': goods}
    return render(request, 'main/index.html', context)

def about(request):
    context = {'title': 'COOKING at HOME - О нас'}
    return render(request, 'main/about.html', context)

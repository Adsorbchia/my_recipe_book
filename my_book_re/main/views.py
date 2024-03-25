
from django.shortcuts import render
from recipe_catalog.models import Category, Recipe
from users.models import User


def index(request):
    categories = Category.objects.all()

    recipes = Recipe.objects.filter(cooking_time__lt=35)[:5]

    context = {
        "title": "COOKING at HOME - Главная",
        "content": "COOKING at HOME - книга полезных рецептов",
        "categories": categories,
        "recipes": recipes,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "COOKING at HOME - О нас"}
    return render(request, "main/about.html", context)


def show_authors(request):
    users = User.objects.all()
    creators = []
    for us in users:
        if us.authors.exists():
             creators.append(us)
    context = {
        "title": "COOKING at HOME - Авторы",
        "creators": creators
    }
    return render(request, 'main/creators.html', context=context)



def show_profile_authors(request, user_id ):
    recipes = Recipe.objects.filter(author=user_id)
    creator = User.objects.get(pk=user_id)
    context = {
        "title": "COOKING at HOME - Страница пользователя",
        "creator": creator,
        "recipes": recipes

    }
    return render(request, 'main/creators_prof.html', context=context)








from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from carts.forms import FavouriteForm
from carts.models import Favourite
from recipe_catalog.models import Recipe

def favorite_recipes(request):
    return render(request, 'carts/favorite_recipes.html')

def cart_add(request, recipe_slug):
        recipe = Recipe.objects.get(slug=recipe_slug)
        if request.user.is_authenticated:
            favorites = Favourite.objects.filter(user=request.user, recipe=recipe)
            if favorites.exists():
                favorites.delete()
            else:
                Favourite.objects.create(user=request.user, recipe=recipe)
           
      
        return redirect(request.META['HTTP_REFERER'])
            
    

      


def cart_remove(request, recipe_slug):
     recipe = Recipe.objects.get(slug=recipe_slug)
     if request.user.is_authenticated:
          favorite = Favourite.objects.filter(user=request.user, recipe=recipe)
          if favorite.exists():
               favorite.delete()
     return redirect(request.META['HTTP_REFERER'])
          




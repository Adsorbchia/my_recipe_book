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
            

def cart_remove(request, cart_id):
    cart = Favourite.objects.get(pk=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
          
def users_recipes(request):
     return render(request, 'carts/user_recipes.html')




from django import template

from carts.models import Favourite
from recipe_catalog.models import Recipe

register = template.Library()

@register.simple_tag()
def favorites_recipes(request):
    return Favourite.objects.filter(user=request.user)

@register.simple_tag()
def user_recipe(request):
    if request.user.is_authenticated:
        return Recipe.objects.filter(author=request.user)


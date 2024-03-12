
from django import template

from carts.models import Favourite

register = template.Library()

@register.simple_tag()
def favorites_recipes(request):
    return Favourite.objects.filter(user=request.user)

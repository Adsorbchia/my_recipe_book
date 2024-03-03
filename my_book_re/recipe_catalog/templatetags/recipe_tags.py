
from django import template
from django.utils.http import urlencode


from recipe_catalog.models import Category, Recipe

register = template.Library()


@register.simple_tag()
def tag_recipes():
    return Recipe.objects.all()


@register.simple_tag()
def tag_category():
    return Category.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    quary = context['request'].GET.dict()
    quary.update(kwargs)
    return urlencode(quary)


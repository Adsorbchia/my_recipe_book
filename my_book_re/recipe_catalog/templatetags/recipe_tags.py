from django import template


from recipe_catalog.models import Category, Recipe

register = template.Library()


@register.simple_tag()
def tag_recipes():
    return Recipe.objects.all()


@register.simple_tag()
def tag_category():
    return Category.objects.all()

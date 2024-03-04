from datetime import datetime
from django.db import models
from django.utils.timezone import utc
from django.urls import reverse

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name_recipe = models.CharField(
        max_length=200, unique=True, verbose_name="Название рецепта"
    )
    slug = models.SlugField(
        max_length=300, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    ingredients = models.CharField(max_length=300, blank=True, null=True, verbose_name="ингредиенты")
    cooking_steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.IntegerField(verbose_name="Время приготовления")
    image = models.ImageField(upload_to="recipe_image", blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    date_of_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления рецепта"
    )
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        db_table = "recipe"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ('id',)

    def __str__ (self):
        return self.name_recipe
  

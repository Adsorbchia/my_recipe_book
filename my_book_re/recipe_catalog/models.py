from datetime import datetime
from django.db import models
from django.utils.timezone import utc
from django.urls import reverse


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


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя")
    surname = models.CharField(max_length=150, unique=True, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    registration_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )

    class Meta:
        db_table = "autors"
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"Автор: {self.name} {self.surname}"


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
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        db_table = "recipe"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ('id',)

    def __str__ (self):
        return self.name_recipe
  

from django.contrib import admin
from django.urls import  path
from recipe_catalog import views

app_name = "recipe_catalog"

urlpatterns = [
    path('search/',views.catalog, name='search' ),
    path("<slug:category_slug>/", views.catalog, name="catalog"),
    path("recipe/<slug:recipe_slug>/", views.recipes, name="recipe"),
    ]

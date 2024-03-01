from django.contrib import admin
from django.urls import include, path
from recipe_catalog import views

app_name = 'recipe_catalog'

urlpatterns = [
   
    path('', views.catalog, name='catalog'),
    path('recipe/', views.recipe, name='recipe' )
]

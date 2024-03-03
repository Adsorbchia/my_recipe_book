
from django.urls import path
from main import views
from recipe_catalog.views import recipes

app_name = "main"


urlpatterns = [
   
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('recipe/', recipes, name='recipe')
]

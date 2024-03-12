from django.urls import path
from carts import views


app_name = "carts"

urlpatterns = [
   path('favorite-recipes/', views.favorite_recipes, name='favorite_recipes'),
    path('cart-add/<slug:recipe_slug>/', views.cart_add, name='cart_add'),
    path('cart-remove/<slug:recipe_slug>/', views.cart_remove, name='cart_remove'),  
]

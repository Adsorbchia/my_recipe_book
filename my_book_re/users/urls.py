from django.urls import path
from users import views


app_name = "users"


urlpatterns = [
   
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('user-settings/', views.user_settings, name='user_settings'),
     path('profile/', views.show_profile, name='profile_user'),
    path('logout/', views.logout, name='logout'),
    path('user-add-recipe/', views.add_recipe, name='user_add_recipe'),
    path('change/<slug:slug_recipe>/', views.change_the_recipe, name='change_the_recipe'),
   path('remove/<slug:slug_recipe>/', views.remove_the_recipe, name='remove' ),
]

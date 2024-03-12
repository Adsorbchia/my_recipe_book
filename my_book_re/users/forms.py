
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from recipe_catalog.models import Recipe


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
                'image','first_name','last_name','username','email',)

    image = forms.ImageField(required=False)   
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()


class UserRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name_recipe',
            'description',
            'ingredients',
            'cooking_steps',
            'cooking_time',
            'image', 
            'category', 'author' ]
    
    

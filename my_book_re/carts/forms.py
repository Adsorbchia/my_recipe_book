
from django import forms

from carts.models import Favourite


class FavouriteForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = ('user', 'recipe',)


from django.db import models
from recipe_catalog.models import Recipe
from users.models import User



class Favourite(models.Model):
    user = models.ForeignKey(User,  blank=True, null=True, verbose_name='пользователь', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, blank=True, null=True, on_delete=models.CASCADE, verbose_name='рецепт')
    class Meta:
        db_table = "favourite"
        verbose_name = "избранное"
        verbose_name_plural = "избранное"

    def __str__(self):
        return f'Избранное {self.user.username} | Рецепт {self.recipe.name_recipe}'





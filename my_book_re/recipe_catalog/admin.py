from django.contrib import admin


from recipe_catalog.models import Author, Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}





@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_recipe',)}

admin.site.register(Author)


# Generated by Django 4.2.10 on 2024-02-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0004_alter_recipe_cooking_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='ингредиенты'),
        ),
    ]
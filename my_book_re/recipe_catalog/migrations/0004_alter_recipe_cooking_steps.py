# Generated by Django 4.2.10 on 2024-02-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0003_author_alter_category_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_steps',
            field=models.TextField(verbose_name='Шаги приготовления'),
        ),
    ]

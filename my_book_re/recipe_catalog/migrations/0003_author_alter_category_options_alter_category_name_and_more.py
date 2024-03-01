# Generated by Django 4.2.10 on 2024-02-29 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0002_alter_category_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Имя')),
                ('surname', models.CharField(max_length=150, unique=True, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Автора',
                'verbose_name_plural': 'Авторы',
                'db_table': 'autors',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_recipe', models.CharField(max_length=200, unique=True, verbose_name='Название рецепта')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('cooking_steps', models.TimeField(verbose_name='Шаги приготовления')),
                ('cooking_time', models.CharField(max_length=20, verbose_name='Время приготовления')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe_image')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления рецепта')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_catalog.author', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'db_table': 'recipe',
            },
        ),
    ]

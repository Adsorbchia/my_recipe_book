# Generated by Django 4.2.10 on 2024-03-11 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_favourites_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favourites',
        ),
    ]

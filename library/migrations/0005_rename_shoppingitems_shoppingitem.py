# Generated by Django 4.2.4 on 2023-09-04 19:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0004_rename_usuario_shopping_user_shoppingitems"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ShoppingItems",
            new_name="ShoppingItem",
        ),
    ]

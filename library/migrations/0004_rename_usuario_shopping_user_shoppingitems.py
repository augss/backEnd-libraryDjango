# Generated by Django 4.2.4 on 2023-09-04 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0003_shopping"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shopping",
            old_name="usuario",
            new_name="user",
        ),
        migrations.CreateModel(
            name="ShoppingItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField(default=1)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="library.book",
                    ),
                ),
                (
                    "shopping",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="library.shopping",
                    ),
                ),
            ],
        ),
    ]

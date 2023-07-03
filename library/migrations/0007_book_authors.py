# Generated by Django 4.2.2 on 2023-07-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0006_rename_appellation_author_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(related_name="books", to="library.author"),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-30 14:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0005_rename_name_author_appellation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="appellation",
            new_name="name",
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-04 18:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["-date_joined"],
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]

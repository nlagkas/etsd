# Generated by Django 3.2.6 on 2021-08-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GlobalPermissionHolder",
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
            ],
            options={
                "permissions": (
                    ("user", "Application user"),
                    ("admin", "Application admin"),
                ),
                "managed": False,
            },
        ),
    ]

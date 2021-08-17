# Generated by Django 3.2.6 on 2021-08-12 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="msgs.messagecategory",
                verbose_name="Category",
            ),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-19 06:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("msgs", "0012_alter_message_local_protocol"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="local_protocol",
        ),
        migrations.AddField(
            model_name="message",
            name="local_identifier",
            field=models.CharField(
                blank=True,
                help_text="Please provide a local identifier (local authority protocol) if needed.",
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9.\\-/]*$", "Valid characters are 0-9 . - /"
                    )
                ],
                verbose_name="Local identifier",
            ),
        ),
    ]

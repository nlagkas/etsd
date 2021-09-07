# Generated by Django 3.2.6 on 2021-09-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0014_auto_20210907_0028"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="kind",
            field=models.CharField(
                choices=[("NEW", "New"), ("REPLY", "Reply"), ("FIX", "Fix")],
                help_text="If you select Reply or Fix you must also select the related message to which you reply or fix",
                max_length=32,
                verbose_name="Message kind",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="protocol",
            field=models.PositiveBigIntegerField(
                blank=True, null=True, verbose_name="Protocol"
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="protocol_year",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Protocol year"
            ),
        ),
        migrations.AlterField(
            model_name="participant",
            name="kind",
            field=models.CharField(
                choices=[
                    ("RECIPIENT", "Recipient (to)"),
                    ("CC", "Carbon Copy (cc)"),
                    ("SENDER", "Sender"),
                ],
                max_length=32,
                verbose_name="Participant kind",
            ),
        ),
        migrations.AlterField(
            model_name="participant",
            name="status",
            field=models.CharField(
                choices=[
                    ("UNREAD", "Unread"),
                    ("READ", "Read"),
                    ("ARCHIVED", "Archived"),
                ],
                default="UNREAD",
                max_length=32,
                verbose_name="Participant status",
            ),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-11 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("keys", "0001_initial"),
        ("authorities", "0003_authority_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="CipherData",
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
                (
                    "cipher_data",
                    models.FileField(
                        upload_to="protected/cipherdata/%Y/%m/%d/",
                        verbose_name="Encrypted data",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cipher data",
                "verbose_name_plural": "Cipher data",
            },
        ),
        migrations.CreateModel(
            name="Data",
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
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created on"),
                ),
                (
                    "modified_on",
                    models.DateTimeField(auto_now=True, verbose_name="Modified on"),
                ),
                ("number", models.PositiveIntegerField()),
                ("content_type", models.CharField(max_length=128)),
            ],
            options={
                "verbose_name": "Message data",
                "verbose_name_plural": "Message data",
            },
        ),
        migrations.CreateModel(
            name="DataAccess",
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
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created on"),
                ),
                (
                    "modified_on",
                    models.DateTimeField(auto_now=True, verbose_name="Modified on"),
                ),
            ],
            options={
                "verbose_name": "Message data access",
                "verbose_name_plural": "Message data accesses",
            },
        ),
        migrations.CreateModel(
            name="Message",
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
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created on"),
                ),
                (
                    "modified_on",
                    models.DateTimeField(auto_now=True, verbose_name="Modified on"),
                ),
                (
                    "available_to_sender",
                    models.BooleanField(
                        default=False,
                        help_text="The message is also encrtypted with the sender's public key",
                        verbose_name="Message is available to sender",
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[("NEW", "New"), ("REPLY", "Reply"), ("FIX", "Fix")],
                        max_length=32,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DRAFT", "Draft"),
                            ("SENT", "Sent"),
                            ("READ", "Read"),
                            ("ARCHIVED", "Archived"),
                            ("DELETED", "Deleted"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "sent_on",
                    models.DateTimeField(blank=True, null=True, verbose_name="Sent on"),
                ),
                ("protocol", models.PositiveBigIntegerField(blank=True, null=True)),
                ("protocol_year", models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
            },
        ),
        migrations.CreateModel(
            name="MessageCategory",
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
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created on"),
                ),
                (
                    "modified_on",
                    models.DateTimeField(auto_now=True, verbose_name="Modified on"),
                ),
                (
                    "name",
                    models.CharField(max_length=64, unique=True, verbose_name="Name"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is active"),
                ),
            ],
            options={
                "verbose_name": "Message Category",
                "verbose_name_plural": "Message Categories",
            },
        ),
        migrations.CreateModel(
            name="Participant",
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
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("RECIPIENT", "Recipient"),
                            ("CC", "Carbon Copy"),
                            ("SENDER", "Sender"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "authority",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="authorities.authority",
                        verbose_name="Authority",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="msgs.message",
                        verbose_name="Message",
                    ),
                ),
            ],
            options={
                "verbose_name": "Message participant",
                "verbose_name_plural": "Message participants",
            },
        ),
        migrations.CreateModel(
            name="ParticipantKey",
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
                (
                    "data",
                    models.ManyToManyField(through="msgs.CipherData", to="msgs.Data"),
                ),
                (
                    "participant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="msgs.participant",
                    ),
                ),
                (
                    "public_key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="keys.publickey"
                    ),
                ),
            ],
            options={
                "verbose_name": "Participant key",
                "verbose_name_plural": "Participant keys",
            },
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-13 12:22

from django.db import migrations, models
import etsd.msgs.models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0005_auto_20210812_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cipherdata',
            name='cipher_data',
            field=models.FileField(upload_to=etsd.msgs.models.cipher_data_upload_to, verbose_name='Encrypted data'),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('SENT', 'Sent')], default='DRAFT', max_length=32),
        ),
    ]

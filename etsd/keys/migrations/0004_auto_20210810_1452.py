# Generated by Django 3.2.6 on 2021-08-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0003_auto_20210810_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='publickey',
            name='user_id',
            field=models.CharField(default='-', help_text='The description (user id) of the key', max_length=128, verbose_name='Description of key'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publickey',
            name='confirmation_document',
            field=models.FileField(blank=True, null=True, upload_to='public/confirmations/%Y/%m/%d/', verbose_name='Confirmation document'),
        ),
        migrations.AlterField(
            model_name='publickey',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REJECTED', 'Rejected')], default='NEW', help_text='Approval status of key', max_length=10, verbose_name='Status'),
        ),
    ]

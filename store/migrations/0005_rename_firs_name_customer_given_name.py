# Generated by Django 4.2.3 on 2023-07-27 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_addres_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firs_name',
            new_name='given_name',
        ),
    ]

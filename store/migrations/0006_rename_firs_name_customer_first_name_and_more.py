# Generated by Django 4.2.3 on 2023-07-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230727_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firs_name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 3.1 on 2020-10-02 15:52

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201002_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=accounts.models.image_upload),
        ),
    ]
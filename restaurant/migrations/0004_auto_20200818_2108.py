# Generated by Django 2.2.9 on 2020-08-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200818_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/menu_images/'),
        ),
    ]

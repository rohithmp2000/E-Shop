# Generated by Django 4.1 on 2022-08-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_order_products_image_alter_products_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]
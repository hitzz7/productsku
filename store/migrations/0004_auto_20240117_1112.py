# Generated by Django 3.2.23 on 2024-01-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_items_price'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='items',
            index=models.Index(fields=['sku', 'status', 'size', 'color', 'price'], name='store_items_sku_3aa0f3_idx'),
        ),
        migrations.AddIndex(
            model_name='productimage',
            index=models.Index(fields=['image'], name='store_produ_image_0fec16_idx'),
        ),
    ]

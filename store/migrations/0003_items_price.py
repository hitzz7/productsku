# Generated by Django 3.2.23 on 2024-01-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_items_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
        ),
    ]
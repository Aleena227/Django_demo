# Generated by Django 5.1.2 on 2024-12-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

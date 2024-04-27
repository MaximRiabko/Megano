# Generated by Django 5.0.3 on 2024-04-11 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0014_alter_review_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productseller",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_seller",
                to="shopapp.product",
            ),
        ),
    ]
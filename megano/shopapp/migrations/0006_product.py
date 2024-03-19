# Generated by Django 5.0.3 on 2024-03-19 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0005_productimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=100)),
                ("description", models.TextField(blank=True)),
                ("archived", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shopapp.categories",
                    ),
                ),
                (
                    "images",
                    models.ManyToManyField(
                        blank=True, related_name="products", to="shopapp.productimage"
                    ),
                ),
                (
                    "preview",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopapp.productimage",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-22 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pay", "0006_alter_order_payment_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"get_latest_by": "created_at"},
        ),
    ]

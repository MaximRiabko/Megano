# Generated by Django 5.0.3 on 2024-05-05 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="role",
            options={"verbose_name": "role", "verbose_name_plural": "roles"},
        ),
    ]
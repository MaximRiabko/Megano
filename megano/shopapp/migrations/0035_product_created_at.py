# Generated by Django 5.0.3 on 2024-05-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0034_alter_profile_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default="2024-05-23 13:00:00"),
            preserve_default=False,
        ),
    ]
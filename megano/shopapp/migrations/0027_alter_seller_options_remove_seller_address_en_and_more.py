# Generated by Django 5.0.3 on 2024-05-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0026_merge_20240503_0742"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="seller",
            options={"verbose_name": "seller"},
        ),
        migrations.RemoveField(
            model_name="seller",
            name="address_en",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="address_ru",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="email_en",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="email_ru",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="image_en",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="image_ru",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="name_en",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="name_ru",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="phone_en",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="phone_ru",
        ),
        migrations.AlterField(
            model_name="seller",
            name="address",
            field=models.CharField(max_length=255, verbose_name="address"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="description",
            field=models.CharField(max_length=255, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="seller_image_directory_path",
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="seller",
            name="name",
            field=models.CharField(max_length=255, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="phone",
            field=models.IntegerField(verbose_name="phone"),
        ),
    ]
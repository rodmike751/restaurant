# Generated by Django 4.1.3 on 2022-11-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_meal_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="in_cart",
            field=models.BooleanField(default=False),
        ),
    ]
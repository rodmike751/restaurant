# Generated by Django 4.1.3 on 2022-11-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="rating",
            field=models.IntegerField(default=80),
        ),
    ]

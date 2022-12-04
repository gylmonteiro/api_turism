# Generated by Django 4.1.3 on 2022-12-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Localization",
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
                ("public_place", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=2)),
                ("country", models.CharField(max_length=2)),
                (
                    "coordenates_latitude",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "coordenates_longitude",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
            ],
        ),
    ]
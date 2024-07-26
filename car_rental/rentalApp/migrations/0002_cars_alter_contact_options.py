# Generated by Django 5.0.6 on 2024-07-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentalApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cars",
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
                ("brand", models.CharField(max_length=255)),
                ("model", models.CharField(max_length=255)),
                ("year", models.IntegerField()),
                ("category", models.IntegerField()),
                ("car_plate", models.CharField(max_length=255)),
                ("mileage", models.FloatField()),
                ("engine_size", models.FloatField()),
                ("fuel", models.CharField(max_length=255)),
                ("gearbox", models.CharField(max_length=255)),
                ("air_contidion", models.BooleanField()),
                ("number_of_seats", models.IntegerField()),
                ("number_of_doors", models.IntegerField()),
                ("color", models.CharField(max_length=255)),
                ("body_style", models.CharField(max_length=255)),
                ("availability", models.BooleanField()),
            ],
            options={
                "verbose_name": "Car For Rental",
                "verbose_name_plural": "Cars For Rental",
            },
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={
                "ordering": ["-timestamp"],
                "verbose_name": "Contact Form",
                "verbose_name_plural": "Contact Forms",
            },
        ),
    ]

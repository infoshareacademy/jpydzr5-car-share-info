from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    email = models.EmailField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"
        ordering = ["-timestamp"]


class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    category = models.IntegerField()
    car_plate = models.CharField(max_length=255)
    mileage = models.FloatField()
    engine_size = models.FloatField()
    fuel = models.CharField(max_length=255)
    gearbox = models.CharField(max_length=255)
    air_contidion = models.BooleanField()
    number_of_seats = models.IntegerField()
    number_of_doors = models.IntegerField()
    color = models.CharField(max_length=255)
    body_style = models.CharField(max_length=255)
    availability = models.BooleanField()

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Car For Rental"
        verbose_name_plural = "Cars For Rental"

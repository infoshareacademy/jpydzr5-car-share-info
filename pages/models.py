from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    email = models.EmailField(max_length=255)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
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
    category = models.CharField(max_length=255)
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
    image = models.ImageField(upload_to="cars_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Car For Rental"
        verbose_name_plural = "Cars For Rental"
        ordering = ["brand", "model"]


class Rental(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    rental_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"Rental of {self.car} by {self.user}"

    class Meta:
        verbose_name = "Car Rental"
        verbose_name_plural = "Car Rentals"
        ordering = ["-rental_date"]

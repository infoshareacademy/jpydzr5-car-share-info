from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    street = models.CharField(max_length=100, blank=True, verbose_name="Street")
    house_number = models.CharField(
        max_length=10, blank=True, verbose_name="House number"
    )
    apartment_number = models.CharField(
        max_length=10, blank=True, verbose_name="Apartment number"
    )
    city = models.CharField(max_length=50, blank=True, verbose_name="City")
    postal_code = models.CharField(max_length=6, blank=True, verbose_name="Postal code")
    username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.email

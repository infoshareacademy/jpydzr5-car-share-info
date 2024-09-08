from django.db import models


# Create your models here.
class RentalLocation(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    @property
    def full_address(self):
        return f"{self.street} {self.postal_code} {self.city}"

    def __str__(self):
        return self.full_address


class RentalPeriod(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    @property
    def full_period(self):
        return f"{self.start_date} {self.start_time} {self.end_date} {self.end_time}"

    def __str__(self):
        return self.full_period


# class RentalAddOn(models.Model):
#     choice = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.choice

class RentalPersonalDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    pesel = models.CharField(max_length=100)
    driving_licence = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone} {self.pesel} {self.driving_licence}"


class RentalPersonalAddress(models.Model):
    personal_street = models.CharField(max_length=100)
    personal_house_number = models.CharField(max_length=100)
    personal_postal_code = models.CharField(max_length=100)
    personal_city = models.CharField(max_length=100)
    personal_country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.personal_street}, {self.personal_house_number} {self.personal_city}, {self.personal_country}"

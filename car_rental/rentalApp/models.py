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

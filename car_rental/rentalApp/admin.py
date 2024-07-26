from django.contrib import admin

from .models import Cars, Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ("full_name", "email", "timestamp")

    def full_name(self, object_):
        return f"{object_.first_name} {object_.last_name}"

    full_name.short_description = "Contact"


admin.site.register(Contact, ContactAdmin)


class CarsAdmin(admin.ModelAdmin):
    model = Cars
    list_display = ("car_name", "category", "availability")

    def car_name(self, object_):
        return f"{object_.brand} {object_.model}"

    car_name.short_description = "Car"


admin.site.register(Cars, CarsAdmin)

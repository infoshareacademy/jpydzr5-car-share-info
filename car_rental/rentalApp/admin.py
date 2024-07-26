from django.contrib import admin

from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ("full_name", "email", "timestamp")

    def full_name(self, object_):
        return f"{object_.first_name} {object_.last_name}"

    full_name.short_description = "Contact"


admin.site.register(Contact, ContactAdmin)

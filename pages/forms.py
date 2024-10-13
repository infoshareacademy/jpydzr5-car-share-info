from django import forms
from .models import Contact, Rental
from django.utils import timezone


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "message": "Message",
            "email": "Email",
            "phone_number": "Phone number",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last name",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your message",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone number (optional)",
                }
            ),
        }
        error_messages = {
            "first_name": {"required": "Please fill in this field."},
            "last_name": {"required": "Please fill in this field."},
            "message": {"required": "Please fill in this field."},
            "email": {"required": "Please fill in this field."},
            "phone_number": {"invalid": "Please enter a valid phone number."},
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields["email"].initial = user.email

        self.fields["phone_number"].required = False


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ["car", "rental_date", "return_date"]
        widgets = {
            "car": forms.Select(attrs={"class": "select form-select", "id": "id_car"}),
            "rental_date": forms.DateInput(attrs={"type": "date"}),
            "return_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["car"].required = False

    def clean_rental_date(self):
        rental_date = self.cleaned_data.get("rental_date")
        if rental_date < timezone.now().date():
            raise forms.ValidationError("Rental date cannot be in the past.")
        return rental_date

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get("car")
        rental_date = cleaned_data.get("rental_date")
        return_date = cleaned_data.get("return_date")

        if not car:
            self.add_error("car", "Car selection is required.")

        if rental_date and return_date:
            if rental_date > return_date:
                self.add_error(
                    "rental_date", "Rental date cannot be later than return date."
                )
                self.add_error(
                    "return_date", "Return date cannot be earlier than rental date."
                )
            elif rental_date == return_date:
                self.add_error(
                    "return_date",
                    "Return date must be at least one day after the rental date.",
                )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user and self.user.is_authenticated:
            instance.user = self.user
        if commit:
            instance.save()
        return instance

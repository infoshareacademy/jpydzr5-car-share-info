from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "message": "Wiadomość",
            "email": "Email",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "first_name": {"required": "Wprowadź poprawne dane."},
            "last_name": {"required": "Wprowadź poprawne dane."},
            "message": {"required": "To pole jest wymagane."},
            "email": {"required": "Wprowadź poprawny adres email."},
        }


# TODO: Override client-side & server-side errors.
# TODO: Dodać miejsce opcjonalne na numer telefonu.

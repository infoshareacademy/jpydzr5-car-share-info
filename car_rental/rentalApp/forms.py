from django import forms
from .models import RentalLocation, RentalPeriod, RentalPersonalDetails, RentalPersonalAddress


class ContactForm(forms.Form):
    firstname = forms.CharField(
        label="Imię",
        error_messages={
            "required": "To pole jest wymagane.",
        },
        widget=forms.TextInput(attrs={"class": "form-control"}),
        # required=False,
    )
    lastname = forms.CharField(
        label="Nazwisko",
        error_messages={"required": "To pole jest wymagane."},
        widget=forms.TextInput(attrs={"class": "form-control"}),
        # required=False,
    )
    comment = forms.CharField(
        label="Wiadomość",
        widget=forms.Textarea(attrs={"class": "form-control"}),
        error_messages={"required": "To pole jest wymagane."},
        # required=False,
    )
    email_address = forms.EmailField(
        label="Adres Email",
        error_messages={"required": "Niepoprawny adres email."},
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        # required=False,
    )


class RentalLocationForm(forms.ModelForm):
    class Meta:
        model = RentalLocation
        fields = ('street', 'postal_code', 'city')


class RentalPeriodForm(forms.ModelForm):
    class Meta:
        model = RentalPeriod
        fields = ('start_date', 'start_time', 'end_date', 'end_time')


# class RentalAddOnForm(forms.Form):
#     class Meta:
#         ADDON_CHOICES = [
#             ('wyjazd_za_granice', 'Wyjazd za granicę'),
#             ('fotelik_dzieciecy', 'Fotelik dziecięcy'),
#             ('dodatkowe_ubezpieczenie', 'Dodatkowe ubezpieczenie'),
#         ]
#         model = RentalAddOn
#         addons = forms.MultipleChoiceField(
#             choices=ADDON_CHOICES,
#             widget=forms.CheckboxSelectMultiple,
#             required=False
#         )


class RentalPersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = RentalPersonalDetails
        fields = ('first_name', 'last_name', 'email', 'phone', 'pesel', 'driving_licence')

class RentalPersonalAddressForm(forms.ModelForm):
    class Meta:
        model = RentalPersonalAddress
        fields = ('personal_street', 'personal_house_number', 'personal_postal_code', 'personal_city', 'personal_country')

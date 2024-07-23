from django import forms

from .models import Contact

# class ContactForm(forms.Form):
#     firstname = forms.CharField(
#         label="Imię",
#         error_messages={
#             "required": "To pole jest wymagane.",
#         },
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         # required=False,
#     )
#     lastname = forms.CharField(
#         label="Nazwisko",
#         error_messages={"required": "To pole jest wymagane."},
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         # required=False,
#     )
#     comment = forms.CharField(
#         label="Wiadomość",
#         widget=forms.Textarea(attrs={"class": "form-control"}),
#         error_messages={"required": "To pole jest wymagane."},
#         # required=False,
#     )
#     email_address = forms.EmailField(
#         label="Adres Email",
#         error_messages={"required": "Niepoprawny adres email."},
#         widget=forms.EmailInput(attrs={"class": "form-control"}),
#         # required=False,
#     )


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
        # BUG: Required field upon deletion allows to submit the form.


# TODO: Client-side required field deletion triggers the display of error messages. It should override default errors.
# TODO: ModelForm with FormView
# TODO: Str representation to modify object

from django import forms


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


# TODO: Client-side required field deletion triggers the display of error messages. It should override default errors.
# TODO: ModelForm

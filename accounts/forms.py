from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
        )


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), required=False
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
            "phone_number",
            "street",
            "house_number",
            "apartment_number",
            "city",
            "postal_code",
        )

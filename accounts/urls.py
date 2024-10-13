from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.user_profile, name="user_profile"),
    path("confirm-email/", views.signup_confirmation, name="signup_confirmation"),
]

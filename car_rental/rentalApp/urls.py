from django.urls import path

from . import views

app_name = "rentalApp"
urlpatterns = [
    path("", views.to_home, name="to_home"),
    path("home/", views.home, name="home"),
    path("rent/", views.rent, name="rent"),
    path("contact/", views.ContactView.as_view(), name="contact"),  # type: ignore
    path("contact/send/", views.send, name="send"),  # type: ignore
]

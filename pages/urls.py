from django.urls import path

from .views import (
    HomePageView,
    RentView,
    ContactView,
    SendView,
    car_detail_api,
    RentalViewSuccess,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("rent/", RentView.as_view(), name="rent"),
    path("rent/<int:car_id>/", RentView.as_view(), name="rent_with_car"),
    path("rental/success/", RentalViewSuccess.as_view(), name="rental_success"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/send/", SendView.as_view(), name="send"),
    path("api/car/<int:pk>/", car_detail_api, name="car_detail_api"),
]

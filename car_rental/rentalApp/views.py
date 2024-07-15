from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def to_home(request):
    return HttpResponseRedirect("home")


def home(request):
    return render(
        request,
        "rentalApp/home.html",
    )


def rent(request):
    return render(
        request,
        "rentalApp/rent.html",
    )


def contact(request):
    return render(
        request,
        "rentalApp/contact.html",
    )

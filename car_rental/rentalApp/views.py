from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm


# Create your views here.
def to_home(request):
    return HttpResponseRedirect(reverse("rentalApp:home"))


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


# TODO: Code Below i.e contact, send


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data  # Storing Cleaned Data
            form.save()
            return render(
                request,
                "rentalApp/contact.html",
                {
                    "form": form,
                },
            )
        else:
            pass  # Handle Errors In Views
    else:
        form = ContactForm()  # Client Side Form Validation

    return render(
        request,
        "rentalApp/contact.html",
        {
            "form": form,
        },
    )


def send(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        comment = request.POST.get("comment")
        email_address = request.POST.get("email_address")
        return render(
            request,
            "rentalApp/send.html",
            {
                "firstname": firstname,
                "lastname": lastname,
                "comment": comment,
                "email_address": email_address,
            },
        )
    if request.method == "GET":
        return HttpResponseRedirect(reverse("rentalApp:contact"))


# TODO: New contact, send

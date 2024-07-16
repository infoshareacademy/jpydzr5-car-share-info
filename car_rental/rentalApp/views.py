from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm


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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # Storing Cleaned Data
            return render(
                request,
                "rentalApp/contact.html",
                {
                    "message": data,
                },
            )
    else:
        form = ContactForm()  # Client Side Form Validation

    return render(
        request,
        "rentalApp/contact.html",
        {
            "form": form,
        },
    )

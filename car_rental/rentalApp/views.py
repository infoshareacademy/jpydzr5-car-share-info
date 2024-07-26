from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

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


class ContactView(FormView):
    form_class = ContactForm
    template_name = "rentalApp/contact.html"
    success_url = "/contact/send/"
    # NOTE: Success url should use reverse funtion

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def send(request):
    return render(request, "rentalApp/send.html")

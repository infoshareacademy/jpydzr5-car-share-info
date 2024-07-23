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


# TODO: BRACKETS
class ContactView(FormView):
    form_class = ContactForm
    template_name = "rentalApp/contact.html"
    success_url = "rentalApp/send.html"
    # success_url = reverse("rentalApp:send")


# TODO: Code Below i.e contact, send


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # data = form.cleaned_data  # Storing Cleaned Data
#             # form.save()
#             return render(
#                 request,
#                 "rentalApp/contact.html",
#                 {
#                     "form": form,
#                 },
#             )
#         else:
#             pass  # Handle Errors In Views
#     else:
#         form = ContactForm()  # Client Side Form Validation

#     return render(
#         request,
#         "rentalApp/contact.html",
#         {
#             "form": form,
#         },
#     )


def send(request):
    if request.method == "POST":
        return render(request, "rentalApp/send.html")
    if request.method == "GET":
        return HttpResponseRedirect(reverse("rentalApp:contact"))


# TODO: New contact, send

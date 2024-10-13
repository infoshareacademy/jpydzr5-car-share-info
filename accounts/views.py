from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages


# Create your views here.


@login_required
def user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("user_profile")
    else:
        form = UserProfileForm(instance=request.user)

    context = {"form": form, "messages": messages.get_messages(request)}
    return render(request, "account/user_profile.html", context)


def signup_confirmation(request):
    return render(request, "account/signup_confirmation.html")

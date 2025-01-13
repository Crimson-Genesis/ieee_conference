from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})


def file_upload_view(request, *args, **kwargs):
    return render(request, "file_upload.html", {})


def profile_view(request, *args, **kwargs):
    return render(request, "profile.html", {})

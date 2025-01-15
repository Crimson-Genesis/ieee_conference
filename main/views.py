from django.http import HttpResponse
from django.shortcuts import render
from .models import Sponsor


def login_view(request, *args, **kwargs):
    context = {"message": "The Login Page."}
    return render(request, "login.html", context)


def register_view(request, *args, **kwargs):
    context = {"message": "The Register Page."}
    return render(request, "register.html", context)


def home_view(request, *args, **kwargs):
    sponsors = Sponsor.objects.all()  # type: ignore
    context = {
        "ieee_sponsors": sponsors,
    }
    return render(request, "home.html", context)


def schedule_view(request, *args, **kwargs):
    context = {"message": "The Schedule Page."}
    return render(request, "schedule.html", context)


def keynote_view(request, *args, **kwargs):
    context = {"message": "The Keynote Page."}
    return render(request, "keynote.html", context)


def about_view(request, *args, **kwargs):
    return render(request, "about.html")


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")


def file_upload_view(request, *args, **kwargs):
    context = {"message": "The File Upload Page."}
    return render(request, "file_upload.html", context)


def profile_view(request, *args, **kwargs):
    context = {"message": "The Profile Page."}
    return render(request, "profile.html", context)

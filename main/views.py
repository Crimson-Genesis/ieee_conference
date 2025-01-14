from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    context = {"message": "Hello, World"}
    return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
    context = {
        "message": "The About Page.",
        "phone": 7247477955,
    }
    return render(request, "about.html", context)


def contact_view(request, *args, **kwargs):
    context = {"message": "The Contact Page."}
    return render(request, "contact.html", context)


def login_view(request, *args, **kwargs):
    context = {"message": "The Login Page."}
    return render(request, "login.html", context)


def register_view(request, *args, **kwargs):
    context = {"message": "The Register Page."}
    return render(request, "register.html", context)


def file_upload_view(request, *args, **kwargs):
    context = {"message": "The File Upload Page."}
    return render(request, "file_upload.html", context)


def profile_view(request, *args, **kwargs):
    context = {"message": "The Profile Page."}
    return render(request, "profile.html", context)


def schedule_view(request, *args, **kwargs):
    context = {"message": "The Schedule Page."}
    return render(request, "schedule.html", context)

def keynote_view(request, *args, **kwargs):
    context = {"message": "The Keynote Page."}
    return render(request, "keynote.html", context)

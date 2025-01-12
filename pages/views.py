from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>This is a Landing page.</h1>")  # type: ignore


def about_view(*args, **kwargs):
    return HttpResponse("<h1>This is a About page.</h1>")  # type: ignore


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>This is a Contact page.</h1>")  # type: ignore

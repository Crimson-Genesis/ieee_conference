from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>This is a Landing page.</h1>") # type: ignore


def about_view(*args, **kwargs):
    return HttpResponse("<h1>This is a Landing page.</h1>")  # type: ignore

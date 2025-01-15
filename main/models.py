from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"  # type: ignore


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(default="http://127.0.0.1:8000/")
    light_logo = models.URLField(
        default="https://duckduckgo.com/i/742895b2644223c0.jpg"
    )
    dark_logo = models.URLField(default="https://duckduckgo.com/i/742895b2644223c0.jpg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name.capitalize()} {self.site}"  # type: ignore


class KeynoteSpeaker(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    topic = models.CharField(max_length=500)
    description = models.TextField(max_length=1000, default="No Body.")

    def __str__(self):
        return f"{self.name}"


class ConferenceTrack(models.Model):
    track_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default="No Body.")

    def __str__(self):
        return f"{self.track_name}"


class Event(models.Model):
    event_name = models.CharField(max_length=100, default="Zero")
    description = models.TextField(max_length=1000, default="No Body.")

    def __str__(self):
        return f"{self.event_name}"


class KeyMilestone(models.Model):
    class Meta:
        ordering = ["date"]

    name = models.CharField(max_length=100, verbose_name="Milestone Name")
    date = models.DateField(verbose_name="Milestone Date")

    def __str__(self):
        return f"{self.name}"

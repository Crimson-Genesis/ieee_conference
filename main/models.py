from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}" #type: ignore

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(default="http://127.0.0.1:8000/")
    light_logo = models.URLField(default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.OAIcrS0Wq9Qrp1920SdZZAHaHa%26pid%3DApi&f=1&ipt=a1055d68c933fe529fb1826cfa1a18f9872e262177a65e0c66f4333151a3b482&ipo=images")
    dark_logo = models.URLField(default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.OAIcrS0Wq9Qrp1920SdZZAHaHa%26pid%3DApi&f=1&ipt=a1055d68c933fe529fb1826cfa1a18f9872e262177a65e0c66f4333151a3b482&ipo=images")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name.capitalize()} {self.site}" #type: ignore

class Events(models.Model): ...


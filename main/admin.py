from django.contrib import admin
from .models import (
    Profile,
    Sponsor,
    KeynoteSpeaker,
    ConferenceTrack,
    Event,
    KeyMilestone,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Sponsor)
admin.site.register(KeynoteSpeaker)
admin.site.register(ConferenceTrack)
admin.site.register(Event)
admin.site.register(KeyMilestone)

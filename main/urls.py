from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("file_upload/", views.file_upload_view, name="file_upload"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about_view, name="about"),
    path("keynote/", views.keynote_view, name="keynote"),
    path("schedule/", views.schedule_view, name="schedule"),
]

from django.urls import path
from .views import *

urlpatterns = [
    path("", view=home, name="home"),
    path("/about-us", view=about, name="about"),
    path("/services", view=services, name="services"),
    path("/hse", view=hse, name="hse"),
    path("/contact", view=contact, name="contact")
]
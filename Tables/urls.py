from django.urls import path
from . import views


app_name = "Tables"
urlpatterns = [
    path("", views.home, name="home"),
]

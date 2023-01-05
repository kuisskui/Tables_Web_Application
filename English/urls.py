from django.urls import path
from . import views


app_name = "English"
urlpatterns = [
    path("", views.home, name="home"),
    path("basic_english/", views.basic_english, name="basic_english"),
    path("basic_english/exercise/<int:unit>", views.exercise, name="exercise"),
    path("basic_english/content/<int:unit>", views.content, name="content"),
]

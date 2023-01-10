from django.urls import path
from .views import *


app_name = "English"
urlpatterns = [
    path("", home, name="home"),
    path("vocabulary/", VocabularyView.as_view(), name="vocabulary"),
    path("vocabulary/create", VocabularyCreateView.as_view(), name="create_vocabulary"),
    path("basic_english/", basic_english, name="basic_english"),
    path("basic_english/exercise/<int:unit>", exercise, name="exercise"),
    path("basic_english/content/<int:unit>", content, name="content"),
]

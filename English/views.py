from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import *
# Create your views here.


def home(request):
    return render(request, "English/home.html")


def basic_english(request):
    return render(request, "English/basic_english/home.html")


class VocabularyView(ListView):
    model = Vocabulary
    template_name = "English/vocabulary/home.html"
    context_object_name = "vocabularies"


class VocabularyCreateView(CreateView):
    model = Vocabulary
    template_name = "English/vocabulary/create.html"
    field = ["word" "word_class"]

    def get_success_url(self) -> str:
        return super().get_success_url()


def exercise(request, unit):
    return render(request, f"English/basic_english/exercises/exercise{unit}.html")


def content(request, unit):
    return render(request, f"English/basic_english/contents/content{unit}.html")

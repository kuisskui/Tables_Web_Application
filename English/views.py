from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "English/home.html")


def basic_english(request):
    return render(request, "English/basic_english/home.html")


def exercise(request, unit):
    return render(request, f"English/basic_english/exercises/exercise{unit}.html")


def content(request, unit):
    return render(request, f"English/basic_english/contents/content{unit}.html")

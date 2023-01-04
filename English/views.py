from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'English/home.html')

def exercise(request, unit):
    return render(request, f'English/basic_english/exercises/exercise{unit}.html')

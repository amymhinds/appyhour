from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse

# Define the home view


def home(request):
    return HttpResponse('<h1>Testing again /ᐠ｡‸｡ᐟ\ﾉ</h1>')

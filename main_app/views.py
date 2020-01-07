from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse

# Define the home view


def home(request):
<<<<<<< HEAD
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def testing(request):
    return HttpResponse('<h1>meow</h1>')
=======
    return HttpResponse('<h1>Testing again /ᐠ｡‸｡ᐟ\ﾉ</h1>')
>>>>>>> 3bc3644ec4b8589bbc2db737a462dd51dd33e68a

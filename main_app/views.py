from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Eater, Review


from django.http import HttpResponse

# Define the home view


def home(request):
    return HttpResponse('<h1>Testing again /ᐠ｡‸｡ᐟ\ﾉ</h1>')


class EaterCreate(CreateView):
    model = Eater
    fields = ['name', 'sex', 'age', 'location', 'interested_in']


class EaterUpdate(UpdateView):
    model = Eater
    fields = ['top_fav_cuisine', 'sec_fav_cuisine',
              'third_fav_cuisine', 'least_fav_cuisine']


class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'


class ReviewUpdate(UpdateView):
    model = Review
    fields = ['about_my_date']


class ReviewDelete(DeleteView):
    model = Review
    success_url = '/reviews/'

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_username(request):
    return HttpResponse('<h1> This is users page </h1> \
                        <a href="/name"> Name is </a>')


def get_name(request):
    return HttpResponse("<h1> My name is Fayzullo </h1> \
                        <a style='color:red; href='/users'>Return Users page </a>")
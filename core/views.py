from django.shortcuts import render
from django.urls.conf import path
from django.urls.resolvers import URLPattern

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home

URLPattern = [
    path('', home, name="home"),
]
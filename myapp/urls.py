from django.contrib import admin
from django.urls import path
from . import views
from .views import scrape_sancionatorio

urlpatterns = [
    path('', scrape_sancionatorio, name='sancionatorio'),
]
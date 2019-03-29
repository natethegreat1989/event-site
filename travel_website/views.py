from events.models import *
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class EventDisplay(ListView):
    template_name = "index.html"
    model = Event


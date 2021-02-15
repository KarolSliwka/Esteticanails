from django.shortcuts import render
from .models import Slide


def home(request):

    slides = Slide.objects.all()

    template = 'home/index.html'
    context = {
        'slides': slides,
    }

    return render(request, template, context)

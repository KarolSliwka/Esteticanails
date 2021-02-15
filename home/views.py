from django.shortcuts import render
from .models import Slides


def home(request):

    slides = Slides.objects.all()

    template = 'home/index.html'
    context = {
        'slides': slides,
    }

    return render(request, template, context)

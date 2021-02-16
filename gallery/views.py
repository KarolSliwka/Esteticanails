from django.shortcuts import render
from .models import GalleryImage


def gallery(request):

    gallery = GalleryImage.objects.all().order_by('-name')

    template = 'gallery/gallery.html'
    context = {
        'gallery': gallery,
    }

    return render(request, template, context)

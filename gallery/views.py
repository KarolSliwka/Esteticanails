from django.shortcuts import render


def gallery(request):

    template = 'gallery/gallery.html'
    context = {}

    return render(request, template, context)

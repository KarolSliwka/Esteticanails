from django.shortcuts import render


def prices(request):

    template = 'prices/prices.html'
    context = {}

    return render(request, template, context)

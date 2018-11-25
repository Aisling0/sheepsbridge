from django.shortcuts import render, get_object_or_404, redirect
from .models import Grooming, Boarding
from django.template.context_processors import csrf


# Create your views here.
def services(request):

    return render(request, "services.html")


def kennels(request):

    return render(request, "kennels.html")


def grooming(request):

    return render(request, "grooming.html")


def prices(request):

    return render(request, 'prices.html', {'boardings': Boarding.objects.all(),
                                           'groomings': Grooming.objects.all()})

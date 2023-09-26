import logging

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
import boto3
from spotlight.forms import SpotlightForm
from spotlight.models import Spotlight

BUCKET_NAME = 'spotlight-16th-ward'


def index(request):
    context = {
        'spotlights': Spotlight.objects.filter(status='S')
    }
    return render(request, 'index.html', context)


def uploadSpotlight(request):
    if request.method == 'POST':
        form = SpotlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect(to='../queue')
    else:
        form = SpotlightForm()
        context = {'form': form}
        return render(request, 'spotlight/uploadSpotlight.html', context)


def spotlightQueue(request):
    context = {'not_started': Spotlight.objects.filter(status='NS'),
               'asked': Spotlight.objects.filter(status='A'),
               'ready': Spotlight.objects.filter(status='R'),
               'planned': Spotlight.objects.filter(status='P'),
               'slacked': Spotlight.objects.filter(status='S')}
    return render(request, 'spotlight/spotlightQueue.html', context)


def editSpotlight(request, id):
    spotlight = Spotlight.objects.get(id=id)
    if request.method == 'POST':
        form = SpotlightForm(request.POST, request.FILES, instance=spotlight)
        if form.is_valid():
            form.save()
    form = SpotlightForm(instance=spotlight)
    context = {
        'spotlight': spotlight,
        'form': form,
    }
    return render(request, 'spotlight/edit.html', context)

def deleteSpotlight(request, id) :
    spotlight = Spotlight.objects.get(id=id)
    if request.method == 'POST':
        spotlight.delete()
        return redirect('queue')
    context = {'spotlight' : spotlight}
    return render(request, 'spotlight/delete.html', context)


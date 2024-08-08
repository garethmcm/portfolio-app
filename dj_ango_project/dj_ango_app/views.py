from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}

    return render(request, 'index.html', context=context)

def audio_index(request):
    context = {}

    return render(request, 'audio_index.html', context=context)
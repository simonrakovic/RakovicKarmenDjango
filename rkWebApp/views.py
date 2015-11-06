# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from rkWebApp.forms import QuestionForm


def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def podjetje(request):
    return render_to_response('podjetje.html', locals(), context_instance=RequestContext(request))

def storitve(request):
    return render_to_response('storitve.html', locals(), context_instance=RequestContext(request))

def povprasevanje(request):

    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            ime_kontaktne_osebe = form.cleaned_data['ime_kontaktne_osebe']

            messages.success(request, 'Povpraševanje uspešno poslano.')
            form = QuestionForm()
            return render_to_response('povprasevanje.html', locals(), context_instance=RequestContext(request))


    return render_to_response('povprasevanje.html', locals(), context_instance=RequestContext(request))

def kontakti(request):
    return render_to_response('kontakti.html', locals(), context_instance=RequestContext(request))


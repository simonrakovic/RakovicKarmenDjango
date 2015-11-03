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

    return render_to_response('povprasevanje.html', locals(), context_instance=RequestContext(request))
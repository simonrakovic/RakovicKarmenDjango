# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
# Create your views here.
from django.template import RequestContext
from rkWebApp.forms import QuestionForm
from rkWebApp.models import Novica, Files


def home(request):

    novice = Novica.objects.all().order_by('-id')[:3]

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
            email = form.cleaned_data['email']
            naziv_podjetja = form.cleaned_data['naziv_podjetja']
            sedez_podjetja = form.cleaned_data['sedez_podjetja'] 
            vrsta_dejavnosti = form.cleaned_data['vrsta_dejavnosti']
            davcni_zavezanec = form.cleaned_data['davcni_zavezanec']
            st_zaposlenih = form.cleaned_data['st_zaposlenih']
            st_prejetnih_racunov = form.cleaned_data['st_prejetnih_racunov']
            st_izdanih_racunov = form.cleaned_data['st_izdanih_racunov'] 
            dodatna_vprasanja = form.cleaned_data['dodatna_vprasanja']
            
            msg = render_to_string('povprasevanje_mail.html', {'ime_kontaktne_osebe':ime_kontaktne_osebe,'email':email,'naziv_podjetja':naziv_podjetja,'sedez_podjetja':sedez_podjetja,'vrsta_dejavnosti':vrsta_dejavnosti,'davcni_zavezanec':davcni_zavezanec,'st_zaposlenih':st_zaposlenih,'st_prejetnih_racunov':st_prejetnih_racunov,'st_izdanih_racunov':st_izdanih_racunov,'dodatna_vprasanja':dodatna_vprasanja})
            
            try:
                msg = EmailMessage('Povprasevanje spletna', msg, email, ['karmen.rakovic@siol.net'])
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
                messages.success(request, 'Povpraševanje je uspešno poslano.')
                form = QuestionForm()
            except:
                messages.success(request, 'Prišlo je do napake!')
                form = QuestionForm()
            
    return render_to_response('povprasevanje.html', locals(), context_instance=RequestContext(request))

def kontakti(request):
    return render_to_response('kontakti.html', locals(), context_instance=RequestContext(request))

def novice(request):

    novice = Novica.objects.all()
    return render_to_response('novice.html', locals(), context_instance=RequestContext(request))

def novica(request, id):

    novica = Novica.objects.get(pk=id)
    files = Files.objects.filter(novica=id)
    return render_to_response('novica.html', locals(), context_instance=RequestContext(request))
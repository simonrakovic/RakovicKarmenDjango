# -*- coding: utf-8 -*-

from django import forms

__author__ = 'simon'

CHOICES = (('1', 'Samostojni podjetnik - s.p.',), ('2', 'mala gospodarska zdruzba - d.o.o.',))
CHOICES2 = (('1', 'Da',), ('2', 'Ne',))

class QuestionForm(forms.Form):

    ime_kontaktne_osebe = forms.CharField(label=u'Ime kontaktne osebe', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=u'E-poštni naslov', widget=forms.TextInput(attrs={'class': 'form-control'}))

    naziv_podjetja = forms.CharField(label=u'Naziv podjetja', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sedez_podjetja = forms.CharField(label=u'Sedež podjetja', widget=forms.TextInput(attrs={'class': 'form-control'}))



    vrsta_dejavnosti = forms.CharField(label=u'Vrsta dejavnosti', widget=forms.TextInput(attrs={'class': 'form-control'}))

    davcni_zavezanec = forms.ChoiceField(label=u'Komitent za DDV', widget=forms.RadioSelect(), choices=CHOICES2)

    st_zaposlenih = forms.CharField(label=u'Število zaposlenih', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))

    st_prejetnih_racunov = forms.CharField(label=u'Število prejetih računov', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))

    st_izdanih_racunov = forms.CharField(label=u'Število izadnih računov', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))


    dodatna_vprasanja = forms.CharField(label=u'Vprašajte nas', widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)


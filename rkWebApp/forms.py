from django import forms

__author__ = 'simon'

CHOICES = (('1', 'Samostojni podjetnik - s.p.',), ('2', 'mala gospodarska zdruzba - d.o.o.',))
CHOICES2 = (('1', 'Da',), ('2', 'Ne',))

class QuestionForm(forms.Form):

    ime_kontaktne_osebe = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'invalid': 'Nepravilen e-postni nsalov.','required': 'Prosim vnesite svoj e-postni naslov.' })

    naziv_podjetja = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sedez_podjetja = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))



    vrsta_podjetja = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES)

    davcni_zavezanec = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES2)

    st_zaposlenih = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    st_prejetnih_racunov = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    st_izdanih_racunov = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


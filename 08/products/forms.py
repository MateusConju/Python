from django import forms
from .models import Products

class ContactForm(forms.Form):
    nome = forms.CharField()
    email = forms.CharField()

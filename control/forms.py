# En tu archivo forms.py
from django import forms
from .models import Control

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = ['nombre', 'estado']

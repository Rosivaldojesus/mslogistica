from django import forms
from django.forms import NumberInput

from .models import ControleFretes

class ControleFretesForm(forms.ModelForm):
    class Meta:
        model = ControleFretes
        fields = '__all__'

    valid = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))


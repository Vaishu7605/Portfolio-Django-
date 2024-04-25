from django import forms 
from .models import *

class contact(forms.ModelForm):
    class Meta:
        model = message
        fields= '__all__' 
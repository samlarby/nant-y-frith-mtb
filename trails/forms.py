from django import forms
from . import models
from .models import Trail 


class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ['name', 'location', 'difficulty', 'description']

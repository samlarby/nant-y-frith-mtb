from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "name",
            "riding_style",
            "favourite_place_to_ride",
            "local_trails",
            "bike",
            "favourite_conditions",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "riding_style": forms.Select(attrs={"class": "form-control"}),
            "favourite_place_to_ride": forms.TextInput(attrs={"class": "form-control"}),
            "local_trails": forms.TextInput(attrs={"class": "form-control"}),
            "bike": forms.TextInput(attrs={"class": "form-control"}),
            "favourite_conditions": forms.Select(attrs={"class": "form-control"}),
        }

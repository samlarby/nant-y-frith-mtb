from django import forms
from django.forms import modelformset_factory
from . import models
from .models import Trail, TrailFeatureImage


# form for adding trails and information, with a background image
class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ['name', 'location', 'difficulty', 'description',
                  'background_image']


class TrailFeatureImageForm(forms.ModelForm):
    class Meta:
        model = TrailFeatureImage
        fields = ['image', 'image_description']


TrailFeatureImageFormSet = modelformset_factory(
    TrailFeatureImage,
    form=TrailFeatureImageForm,
    extra=1,
    can_delete=1,
)
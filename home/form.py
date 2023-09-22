from django import forms
from .models import report_image
from django.forms import ModelForm

class ImageForm(forms.ModelForm):
    class Meta:
        model=report_image
        fields=("image",)
         

    
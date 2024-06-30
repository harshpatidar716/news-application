from django import forms
from .models import reporter_img


class ImageForm(forms.ModelForm):
    class Meta:
        model = reporter_img
        fields = ("image", "username")

from django import forms
from .models import reporter_img
from .models import advertisement


class ImageForm(forms.ModelForm):
    class Meta:
        model = reporter_img
        fields = ("image",)


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = advertisement
        fields = ("image",)

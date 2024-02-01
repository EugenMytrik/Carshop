from django import forms

from .models import Car


class CarPhotoChangeForm:
    photo = forms.ImageField(label="Choose image: ", widget=forms.FileInput)

    class Meta:
        model = Car
        fields = ("photo",)

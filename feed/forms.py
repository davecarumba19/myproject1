from typing import Text
from django import forms


class PostForm(forms.Form):
    text = forms.CharField(label="Title")
    image = forms.FileField(label="Upload Image ")
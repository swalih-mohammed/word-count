from django.forms import ModelForm, TextInput
from django import forms


class URLForm(forms.Form):
    # url = forms.CharField(max_length=250)
    url = forms.CharField(max_length=250)

    # class Meta:
    #     fields = ['url']
    #     widgets = {'url': TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'URL'})}

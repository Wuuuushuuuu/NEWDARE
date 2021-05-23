from django.forms import ModelForm
from Client.models import client
from django import forms


class SaveClientRecord(ModelForm):
    class Meta:
        model = client
        fields = ['name', 'email', 'contact_no']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'size':50}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'size':50}),
            'contact_no': forms.TextInput(attrs={'placeholder': 'Contact Number', 'size':50}),
     }
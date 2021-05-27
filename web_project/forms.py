from django.forms import ModelForm
from Client.models import client
from django import forms
from Client.models import Bookings


class SaveClientRecord(ModelForm):
    class Meta:
        model = client
        fields = ['name', 'email', 'contact_no']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'size':50}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'size':50}),
            'contact_no': forms.TextInput(attrs={'placeholder': 'Contact Number', 'size':50}),
     }

class ContactForm(forms.Form):
	Name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class UpdateForm(ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'

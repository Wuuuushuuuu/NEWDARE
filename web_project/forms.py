from django.forms import ModelForm
from Client.models import client
from django import forms
from Client.models import Bookings, Invoice


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
        fields = {'Name', 'Contact_no', 'Date','Concern','time','Status'}
        widgets = {
            'Name': forms.TextInput(attrs={'size':50}),
            'Contact_no': forms.TextInput(attrs={ 'size':50}),
            'Date': forms.TextInput(attrs={ 'size':50}),
            'Concern': forms.TextInput(attrs={ 'size':50}),
            'time': forms.TextInput(attrs={ 'size':50}),
         }

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = {'Name', 'Contact_no', 'Date','Concern','Amount_Due'}
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Name','size':50}),
            'Contact_no': forms.TextInput(attrs={'placeholder': 'Contact Number', 'size':50}),
            'Date':forms.TextInput(attrs={'placeholder':'MM/DD/YY', 'size':50}),
            'Amount_Due': forms.TextInput(attrs={'placeholder': 'Amount Due', 'size':50}),
         }
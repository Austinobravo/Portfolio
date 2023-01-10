from django import forms
from .models import *

#Creating The contact form
class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Your Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email','placeholder':"Your Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':30, 'rows':10, 'placeholder':"Write Message Here..."}))

    class Meta:
        model = Contact
        fields = '__all__'
        
    
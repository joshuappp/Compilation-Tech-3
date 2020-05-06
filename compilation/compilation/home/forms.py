from django import forms
from .models import ContactUs




class ContactUsModelForm(forms.ModelForm):

	fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
	contact  = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
	email    = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}))

	class Meta:
		model = ContactUs
		fields = ('fullname','contact','email','description')
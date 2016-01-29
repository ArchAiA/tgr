from django import forms
from .models import ContactInfo

class ContactInfoForm(forms.ModelForm):
	class Meta:
		model = ContactInfo
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

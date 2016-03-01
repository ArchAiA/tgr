from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ContactInfo(models.Model):
	full_name = models.CharField(max_length=120, blank=False, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name
		
	def __unicode__(self):
		return self.email

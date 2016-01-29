from django.contrib import admin
from .models import ContactInfo
from .forms import ContactInfoForm


# Register your models here.

class ContactInfoAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp', 'updated']
	form = ContactInfoForm
from django.shortcuts import render
from .forms import ContactInfoForm
# Create your views here.


def newsletter(request):
	context = {}
	return render(request, 'contact.html', context)
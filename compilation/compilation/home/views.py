from django.shortcuts import render
from .forms import ContactUsModelForm

def home_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'home/home_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)


def about_us_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'home/about_us_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)
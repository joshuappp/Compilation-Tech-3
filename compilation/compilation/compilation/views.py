from django.shortcuts import render
from residence.forms import ContactUsModelForm

def compilation_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   print(contactus_form.cleaned_data)
	   contactus_form = ContactUsModelForm()

	template_name = 'compilation.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)


def about_us_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   print(contactus_form.cleaned_data)
	   contactus_form = ContactUsModelForm()

	template_name = 'about_us_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)
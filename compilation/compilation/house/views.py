from django.shortcuts import render,get_object_or_404,redirect
from .forms import FindHouseModelForm,UploadHouseModelForm,ContactUsModelForm
from .models import UploadHouse

# Create your views here.

def find_house_view(request):

	findhouse_form = FindHouseModelForm(request.POST or None)
	contactus_form = ContactUsModelForm(request.POST or None)
	popup_message = False
	province = ''
	location = ''
	section  = ''

	if findhouse_form.is_valid():
	   query = findhouse_form.cleaned_data
	   house_list = UploadHouse.objects.search(query)

	   if len(house_list) !=0:

		   province = house_list[0].province
		   location = house_list[0].location
		   section = house_list[0].section

		   return redirect('/house/available_houses/{}/{}/{}/'.format(province,location,section))

	   else:
	    	popup_message = True
	    	province = query['province']
	    	location = query['location']
	    	section  = query['section']


	   
	   findhouse_form = FindHouseModelForm()

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'house/find_house_main.html'
	context = {
	    'findhouse_form': findhouse_form,
	    'contactus_form': contactus_form,
	    'popup_message': popup_message,
	    'province': province,
		'location': location,
		'section': section,
	}

	return render(request,template_name,context)

def upload_house_view(request):

	uploadhouse_form = UploadHouseModelForm(request.POST or None, request.FILES or None)
	contactus_form = ContactUsModelForm(request.POST or None)
	popup_message_success = False


	if uploadhouse_form.is_valid():
	   uploadhouse_form.save()
	   popup_message_success = True
	   uploadhouse_form = UploadHouseModelForm()

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'house/upload_house_main.html'
	context = {
	    'uploadhouse_form': uploadhouse_form,
	    'contactus_form': contactus_form,
	    'popup_message_success':popup_message_success
	}

	return render(request,template_name,context)

def available_houses_view(request):

	list_of_avai_houses = []

	queryset = UploadHouse.objects.all()


	for ele in queryset:
		image_path = str(ele.image)

		index = image_path.find('house/') +6

		image = image_path[index:]

		list_of_avai_houses.append({'province':ele.province,'location':ele.location,'section':ele.section,'address':ele.address,'price':ele.price,'contact':ele.contact,'image':image})

	data_available = True

	if len(list_of_avai_houses) !=0:

		province = list_of_avai_houses[0]['province']
		location = list_of_avai_houses[0]['location']

	else:
		data_available = False
		province = ''
		location = ''



	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'house/available_houses_main.html'
	context = {
		'province': province,
		'location': location,
	    'object_list':list_of_avai_houses,
	    'contactus_form': contactus_form,
	    'data_available': data_available,
	}


	return render(request,template_name,context)

def match_available_houses_view(request,province,location,section):

	list_of_avai_houses = []
	data_available = False

	query = {
	   'province':province,
	   'location':location,
	   'section':section
	}

	house_list = UploadHouse.objects.search(query)

	if len(house_list) !=0:

		for ele in house_list:
			image_path = str(ele.image)

			index = image_path.find('house/') +6

			image = image_path[index:]

			list_of_avai_houses.append({'province':ele.province,'location':ele.location,'section':ele.section,'address':ele.address,'price':ele.price,'contact':ele.contact,'image':image})

			data_available = True

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'house/available_houses_main.html'
	context = {
		'province': province,
		'location': location,
	    'object_list':list_of_avai_houses,
	    'contactus_form': contactus_form,
	    'data_available': data_available,
	}


	return render(request,template_name,context)



def about_house_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'house/about_us_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)



















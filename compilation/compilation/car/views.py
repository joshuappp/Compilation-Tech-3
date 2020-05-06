from django.shortcuts import render,get_object_or_404,redirect
from .forms import FindCarModelForm,UploadCarModelForm,ContactUsModelForm
from .models import UploadCar
# Create your views here.

def find_car_view(request):

	findcar_form = FindCarModelForm(request.POST or None)
	contactus_form = ContactUsModelForm(request.POST or None)
	popup_message = False
	province = ''
	location = ''
	section  = ''


	if findcar_form.is_valid():
	   query = findcar_form.cleaned_data
	   car_list = UploadCar.objects.search(query)

	   if len(car_list) !=0:

		   province = car_list[0].province
		   location = car_list[0].location
		   section = car_list[0].section

		   return redirect('/car/available_cars/{}/{}/{}/'.format(province,location,section))

	   else:
	    	popup_message = True
	    	province = query['province']
	    	location = query['location']
	    	section  = query['section']


	   
	   findcar_form = FindCarModelForm()

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'car/find_car_main.html'
	context = {
	    'findcar_form': findcar_form,
	    'contactus_form': contactus_form,
	    'popup_message': popup_message,
	    'province': province,
		'location': location,
		'section': section,
	}

	return render(request,template_name,context)

def upload_car_view(request):

	uploadcar_form = UploadCarModelForm(request.POST or None, request.FILES or None)
	contactus_form = ContactUsModelForm(request.POST or None)
	popup_message_success = False


	if uploadcar_form.is_valid():
	   uploadcar_form.save()
	   popup_message_success = True
	   uploadcar_form = UploadCarModelForm()

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'car/upload_car_main.html'
	context = {
	    'uploadcar_form': uploadcar_form,
	    'contactus_form': contactus_form,
	    'popup_message_success': popup_message_success
	}

	return render(request,template_name,context)

def available_cars_view(request):

	list_of_avai_rooms = []

	queryset = UploadCar.objects.all()


	for ele in queryset:
		image_path = str(ele.image)

		index = image_path.find('car/') +4

		image = image_path[index:]

		list_of_avai_rooms.append({'province':ele.province,'location':ele.location,'section':ele.section,'address':ele.address,'price':ele.price,'contact':ele.contact,'image':image})

	data_available = True

	if len(list_of_avai_rooms) !=0:

		province = list_of_avai_rooms[0]['province']
		location = list_of_avai_rooms[0]['location']

	else:
		data_available = False
		province = ''
		location = ''



	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'car/available_cars_main.html'
	context = {
		'province': province,
		'location': location,
	    'object_list':list_of_avai_rooms,
	    'contactus_form': contactus_form,
	    'data_available': data_available,
	}


	return render(request,template_name,context)

def match_available_cars_view(request,province,location,section):

	list_of_avai_cars = []
	data_available = False

	query = {
	   'province':province,
	   'location':location,
	   'section':section
	}

	car_list = UploadCar.objects.search(query)

	if len(car_list) !=0:

		for ele in car_list:
			image_path = str(ele.image)

			index = image_path.find('car/') +4

			image = image_path[index:]

			list_of_avai_cars.append({'province':ele.province,'location':ele.location,'section':ele.section,'address':ele.address,'price':ele.price,'contact':ele.contact,'image':image})

			data_available = True

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'car/available_cars_main.html'
	context = {
		'province': province,
		'location': location,
	    'object_list':list_of_avai_cars,
	    'contactus_form': contactus_form,
	    'data_available': data_available,
	}


	return render(request,template_name,context)

def about_us_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'car/about_us_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)





















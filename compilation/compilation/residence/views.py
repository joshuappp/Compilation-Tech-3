from django.shortcuts import render,get_object_or_404,redirect
from .forms import FindRooMModelForm,UploadRoomModelForm,ContactUsModelForm
from .models import UploadRoom
# Create your views here.

def find_room_view(request):

	findroom_form = FindRooMModelForm(request.POST or None)
	contactus_form = ContactUsModelForm(request.POST or None)
	popup_message = False
	province = ''
	location = ''
	section  = ''

	if findroom_form.is_valid():
	   query = findroom_form.cleaned_data

	   residence_list = UploadRoom.objects.search(query)

	   if len(residence_list) !=0:

		   province = query['province']
		   location = query['location']
		   section = query['section']

		   return redirect('/residence/available_rooms/{}/{}/{}/'.format(province,location,section))

	   else:
	    	popup_message = True
	    	province = query['province']
	    	location = query['location']
	    	section  = query['section']


	   
	   findroom_form = FindRooMModelForm()

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'room/find_room_main.html'
	context = {
	    'findroom_form': findroom_form,
	    'contactus_form': contactus_form,
	    'popup_message': popup_message,
	    'province': province,
		'location': location,
		'section': section,
	}

	return render(request,template_name,context)

def upload_room_view(request):

	uploadroom_form = UploadRoomModelForm(request.POST or None, request.FILES or None)
	contactus_form = ContactUsModelForm(request.POST or None)
	popup_message_success = False


	if uploadroom_form.is_valid():
	   uploadroom_form.save()
	   popup_message_success =  True,
	   uploadroom_form = UploadRoomModelForm()

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'room/upload_room_main.html'
	context = {
	    'uploadroom_form': uploadroom_form,
	    'contactus_form': contactus_form,
	    'popup_message_success': popup_message_success
	}

	return render(request,template_name,context)

def available_rooms_view(request):

	list_of_avai_rooms = []

	queryset = UploadRoom.objects.all()


	for ele in queryset:
		image_path = str(ele.image)

		index = image_path.find('residence/') +10

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

	template_name = 'room/available_rooms_main.html'
	context = {
		'province': province,
		'location': location,
	    'object_list':list_of_avai_rooms,
	    'contactus_form': contactus_form,
	    'data_available': data_available,
	}


	return render(request,template_name,context)

def match_available_rooms_view(request,province,location,section):

	list_of_avai_rooms = []
	data_available = False

	query = {
	   'province':province,
	   'location':location,
	   'section':section
	}

	residence_list = UploadRoom.objects.search(query)

	if len(residence_list) !=0:

		for ele in residence_list:
			image_path = str(ele.image)

			index = image_path.find('residence/') +10

			image = image_path[index:]

			list_of_avai_rooms.append({'province':ele.province,'location':ele.location,'section':ele.section,'address':ele.address,'price':ele.price,'contact':ele.contact,'image':image})

			data_available = True

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'room/available_rooms_main.html'
	context = {
		'province': province,
		'location': location,
	    'object_list':list_of_avai_rooms,
	    'contactus_form': contactus_form,
	    'data_available': data_available,
	}


	return render(request,template_name,context)

def about_us_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   contactus_form.save()
	   contactus_form = ContactUsModelForm()

	template_name = 'room/about_us_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)





















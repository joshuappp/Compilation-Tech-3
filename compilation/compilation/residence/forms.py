from django import forms
from  .models import FindRoom,UploadRoom,ContactUs


class FindRooMModelForm(forms.ModelForm):

	PROVINCES = (
	    ('gauteng', 'Gauteng'),
	    ('north_west', 'North West'),
	    ('mpumalanga', 'Mpumalanga'),
	    ('kwazuli_natal', 'Kwazulu Natal'),
	    ('western_cape', 'Western Cape'),
	    ('limpopo', 'Limpopo'),
	    ('northern_cape', 'Northen Cape'),
	    ('free_state', 'Free State'),
	    ('eastern_cape', 'Eastern Cape')
	)

	province = forms.ChoiceField(choices=PROVINCES)
	location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Soweto'}))
	section = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Bara'}))

	class Meta:

		model = FindRoom
		fields = ('province', 'location', 'section')

class UploadRoomModelForm(forms.ModelForm):

	PROVINCES = (
	    ('gauteng', 'Gauteng'),
	    ('north_west', 'North West'),
	    ('mpumalanga', 'Mpumalanga'),
	    ('kwazuli_natal', 'Kwazulu Natal'),
	    ('western_cape', 'Western Cape'),
	    ('limpopo', 'Limpopo'),
	    ('northern_cape', 'Northen Cape'),
	    ('free_state', 'Free State'),
	    ('eastern_cape', 'Eastern Cape')
	)

	province = forms.ChoiceField(choices=PROVINCES)
	location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Soweto'}))
	section = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Bara'}))
	address  = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Main Street...'}))
	price    = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'e.g 2000.00'}))
	contact  = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
	


	class Meta:
		model = UploadRoom
		fields = ('province','location','section','address','price','contact','image',)


class ContactUsModelForm(forms.ModelForm):

	fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
	contact  = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
	email    = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}))

	class Meta:
		model = ContactUs
		fields = ('fullname','contact','email','description')

			

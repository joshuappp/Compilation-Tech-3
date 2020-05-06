from django.db import models

class ContactUs(models.Model):

	fullname    = models.CharField(max_length=60,blank=False,null=False)
	contact     = models.IntegerField(blank=False,null=False)
	email       = models.EmailField(max_length=50,blank=False,null=False)
	description = models.CharField(max_length=100,blank=True,null=True)


		

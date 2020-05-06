from django.db import models
from django.db.models import Q

# Create your models here.
class HousePostQuerySet(models.QuerySet):

    def search(self, query):

        lookup = (Q(province__iexact=query['province']) &
                  Q(location__iexact=query['location']) &
                  Q(section__iexact=query['section']) 
                  )

        if len(self.filter(lookup)) == 0:

            lookup = (Q(province__icontains=query['province']) &
                      Q(location__icontains=query['location']) |
                      Q(section__icontains=query['section']) 
                      )

            return self.filter(lookup)

        return self.filter(lookup)


class HousePostManager(models.Manager):

    def get_queryset(self):
        return HousePostQuerySet(self.model, using=self._db)

    def search(self, query = None):

        if query is None:
            return self.get_queryset().none()

        return self.get_queryset().search(query)

class FindHouse(models.Model):

    province = models.CharField(max_length=30,blank=False,null=False)
    location = models.CharField(max_length=40,blank=False,null=False)
    section  = models.CharField(max_length=40,blank=False,null=False)

class UploadHouse(models.Model):

    province = models.CharField(max_length=30,blank=False,null=False)
    location = models.CharField(max_length=40,blank=False,null=False)
    section  = models.CharField(max_length=40,blank=False,null=False)
    address  = models.CharField(max_length=60,blank=False,null=False)
    price    = models.DecimalField(decimal_places=2,max_digits=10,blank=False,null=False)
    contact  = models.IntegerField(blank=False,null=False)
    image    = models.ImageField(upload_to='home/static/img/house/',blank=False,null=False)

    objects = HousePostManager()




class ContactUs(models.Model):

	fullname    = models.CharField(max_length=60,blank=False,null=False)
	contact     = models.IntegerField(blank=False,null=False)
	email       = models.EmailField(max_length=50,blank=False,null=False)
	description = models.CharField(max_length=100,blank=True,null=True)


		

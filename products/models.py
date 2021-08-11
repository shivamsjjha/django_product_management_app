from django.db import models
from datetime import datetime
#from taggit.managers import TaggableManager


class TurorialCategory(models.Model):
	tutorial_category=models.CharField(max_length=100)
	category_summary=models.CharField(max_length=200)
	category_slug=models.CharField(max_length=100)

	def __str__(self):
		return self.tutorial_category

class TurorialSeries(models.Model):
	tutorial_series=models.CharField(max_length=200)
	tutorial_category=models.ForeignKey(TurorialCategory,default=1,on_delete=models.SET_DEFAULT)
	series_summary=models.CharField(max_length=100)

	def __str__(self):
		return self.tutorial_series


class Turorial(models.Model):
	title=models.CharField(max_length=100,null=True)
	content= models.TextField(null= True, blank=True)
	published=models.DateTimeField(default=datetime.now())
	tutorial_series=models.ForeignKey(TurorialSeries,default=1,on_delete=models.SET_DEFAULT)
	tutorial_slug=models.CharField(max_length=100,default=1)

	def __str__(self):
		return self.title


		

class Body(models.Model):
	image=models.ImageField(upload_to='pics')
	description= models.TextField(null= True, blank=True)
	featured=models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now =True)

	def __str__(self):
		return self.description





















"""class Blog(models.Model):
	title=models.TextField(null=False, blank=False,max_length=500)
	author=models.CharField(max_length=100, null=False,blank=False, default='Unknown')
	image=models.ImageField(upload_to='youtube',null=True,blank=True)
	post=models.TextField(null=False, blank=False)
	featured=models.BooleanField(default=True)
	published = models.DateField(auto_now_add=True)
	tags = TaggableManager()

	def __unicode__(self):
		return str(self.title)

"""


#class Places(models.Model):
#	name = models.CharField(max_length=30, null=False, blank= False)
#	image=models.ImageField(upload_to='images')
#	description= models.TextField(null= True, blank= True)
#	price = models.DecimalField(decimal_places=2,max_digits=10,default=False)
#	active= models.BooleanField(default=True)
#	featured=models.BooleanField(default=True)
#	timestap = models.DateTimeField(auto_now_add = True, auto_now =False)
#	updated = models.DateTimeField(auto_now_add = False, auto_now =True)



#	def __unicode__(self):
#		return str(self.name)
#
#	def get_price(self):
#		return (self.price)



#class DiscountField(models.Model):
#	discountfield=models.ForeignKey(Places,on_delete=models.CASCADE)
#	discount = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
#	new_price = models.DecimalField(decimal_places=2,max_digits=10,default=False)










# Create your models here.
#class Product(models.Model):
#	title = models.CharField(max_length=100, null=False, blank= False)
#	description= models.TextField(null= True, blank= True)
#	price = models.DecimalField(decimal_places=2,max_digits=100,default=30.00)
#	discount = models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
#	slug = models.SlugField()
#	timestap = models.DateTimeField(auto_now_add = True, auto_now =False)
#	updated = models.DateTimeField(auto_now_add = False, auto_now =True)
#	active= models.BooleanField(default=True)
#	pid=models.IntegerField(default=0)
		
#	def __unicode__(self):
#		return str(self.title)

#	def get_price(self):
#		return (self.price)


#class ProductImage(models.Model):
#	product=models.ForeignKey(Product,on_delete=models.CASCADE)
#	image=models.ImageField(upload_to='img')
#	featured=models.BooleanField(default=True)
#	thumbnail=models.BooleanField(default=False)
#	active= models.BooleanField(default=True)
#	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

#	def __unicode__(self):
#		return self.Product.title


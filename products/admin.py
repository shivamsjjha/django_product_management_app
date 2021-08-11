# Register your models here.
from django.contrib import admin
from .models import Body,TurorialCategory,TurorialSeries,Turorial

class ProductAdmin(admin.ModelAdmin):
	list_display=['title','tutorial_slug','published']	
	class Meta:
		model= Turorial

admin.site.register(Body)
admin.site.register(TurorialSeries)
admin.site.register(TurorialCategory)
admin.site.register(Turorial,ProductAdmin)





























#class PlaceAdmin(admin.ModelAdmin):
#	search_fields=['name','description']
#	list_editable=['price','active','featured']
#	class Meta:
#		model= Places

#class BodyAdmin(admin.ModelAdmin):
#	search_fields=['description']
#	list_display=['description','featured','updated']
#	list_editable=['description','featured']
#	class Meta:
#		model= Body

#class QuotepicsAdmin(admin.ModelAdmin):
#	search_fields=['description']
#	list_display=['description','featured']
#	list_editable=['description','featured']
#	class Meta:
#		model= Quotepics




#admin.site.register(Places,PlacesAdmin)
#admin.site.register(DiscountField)



#from . import models
#from .models import Places,DiscountField,Body,Quotepics















#from .models import Product,ProductImage,HomePage

#class ProductAdmin(admin.ModelAdmin):
#	search_fields=['title','description','slug']
#	list_display=['title','price','active','updated']
#	list_editable=['price','active']
#	class Meta:
#		model= Product

#admin.site.register(Product,ProductAdmin)

#admin.site.register(ProductImage)

#admin.site.register(HomePage)
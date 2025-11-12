from django.contrib import admin
from firstapp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=['user','is_vendor','phonenumber','address','created_at']
    list_per_page=15
    
admin.site.register(Profile,UserAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display=['user','store_desc','store_logo','subscription_plan','subscription_expiry','created_at','updated_at']
    list_per_page=15
admin.site.register(Vendor,VendorAdmin)

class CatAdmin(admin.ModelAdmin):
    list_display=['cat_name','slug','parent']
    list_per_page=15
admin.site.register(Category,CatAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_description','brand','created_at']
    list_per_page=15
admin.site.register(Products,ProductAdmin)

class VendorProductAdmin(admin.ModelAdmin):
    list_display=['vendor','products','price','stock','listed_at']
    list_per_page=15
admin.site.register(vendorProduct,VendorProductAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display=['Image']
    list_per_page=15
admin.site.register(Image,ImageAdmin)
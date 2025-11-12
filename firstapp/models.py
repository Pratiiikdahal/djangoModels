from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_vendor=models.BooleanField(default=False)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    store_name=models.CharField(max_length=100)
    store_desc=models.TextField(max_length=150,blank=True,null=True)
    store_logo=models.ImageField(upload_to='vendor_image/',null=True,blank=True)
    subscription_plan=models.CharField(max_length=50,choices=[('basic','Basic'),('premium','Premium'),('enterprise','Enterprise')],default='basic')
    subscription_expiry=models.CharField(max_length=50,blank=True,null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.store_name
    
class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,related_name='category')  #for reverse query as you can access the category even as a sub category fi ever needed to do so
    
    def __str__(self):
        return  self.cat_name

class Image(models.Model):
    Image=models.ImageField(upload_to='product-images/',null=True,blank=True)   
    
class Products(models.Model):
    product_name=models.CharField(max_length=50)
    product_description=models.TextField(max_length=100,blank=True,null=True)
    brand=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    Image=models.ForeignKey(Image,on_delete=models.PROTECT,null=True,blank=True)
    Category=models.ManyToManyField(Category,related_name='products')
    #string representation in the superadmin
    def __str__(self):
        return self.product_name

class vendorProduct(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)  
    price=models.FloatField()
    stock=models.IntegerField(default=0)
    listed_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vendor.store_name} - {self.product.name}"
      
      

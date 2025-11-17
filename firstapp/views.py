from django.shortcuts import render
from firstapp.models import *
# Create your views here.

def index(request):
    Product=Products.objects.all()[:4]
    context={'product':Product}
    return render(request,'firstapp/index.html',context=context)
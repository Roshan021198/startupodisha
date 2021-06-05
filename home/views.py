from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,JsonResponse
from .models import IndustryPartner

# Create your views here.

def index(request):
    logo = IndustryPartner.objects.all()
    return render(request,'index.html',{'logo':logo})
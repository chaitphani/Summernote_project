from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from NJnaiduapp.models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
# from myproject.utils import is_authenticated
from random import randint
from django.core.mail import send_mail
from  NJnaiduportal import settings
import socket
from django.db.models import Q
import datetime
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from NJnaiduapp.forms import *



def contact(request):
    return render(request, {})

def index(request):
    category=Category.objects.all()
    items=Item.objects.all()
    sec1=Section1.objects.all()
    sec2=Section2.objects.all()
    Whyus=WhyUs.objects.all()
    specialities=Specialities.objects.all()
    spec=Specialities.objects.all()[:3]
    spe=Procedure.objects.all()[:4]
    return render(request, 'index.html',{'category':category,'items':items,'sec1':sec1,'sec2':sec2,
    'whyus':Whyus,'specialities':specialities,'spec':spec,'spe':spe})


def specialities(request,slug):
    category=Category.objects.all()
    specialities=Specialities.objects.all()
    spc=Specialities.objects.filter(slug=slug)
    return render(request,'speciality.html',{'category':category,'spc':spc,'specialities':specialities})

def category(request,slug):
    category=Category.objects.all()
    specialities=Specialities.objects.all()
    cat=Category.objects.filter(slug=slug)
    return render(request,'category.html',{'category':category,'specialities':specialities,'cat':cat})

def items(request,slug):
    category=Category.objects.all()
    specialities=Specialities.objects.all()
    item=Item.objects.filter(slug=slug)
    return render(request,'item.html',{'category':category,'specialities':specialities,'items':item})

def event(request):
    category=Category.objects.all()
    specialities=Specialities.objects.all()
    event=Event.objects.all()
    images=Images.objects.all()
    return render(request,'gallery.html',{'category':category,'specialities':specialities,'event':event,'images':images})

def procedure(request,slug):
    category=Category.objects.all()
    specialities=Specialities.objects.all()
    pro=Procedure.objects.filter(slug=slug)
    return render(request,'procedure.html',{'category':category,'specialities':specialities,'pro':pro})


def our_team(request):
    category=Category.objects.all()
    specialities=Specialities.objects.all()
    team=Ourteam.objects.all()
    spec=Specialities.objects.all()
    return render(request,'ourteam.html',{'category':category,'specialities':specialities,'team':team,'spec':spec}) 
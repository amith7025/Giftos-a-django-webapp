from django.shortcuts import render,redirect
from Home_page.models import ITEMDATABASE
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):

    dests = ITEMDATABASE.objects.all()
    return render(request,'index.html',{'dests':dests})

def contact(request):
    return render(request,'contact.html')

def why(request):
    return render(request,'why.html')

def testimonial(request):
    return render(request,'testimonial.html')

def shop(request):
    dests = ITEMDATABASE.objects.all()
    return render(request,'shop.html',{'dests':dests})


def logout_fun(request):
    auth.logout(request)
    return redirect('/')
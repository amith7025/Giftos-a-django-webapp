from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('happening')
            return redirect('home/home')
            
        else:
            return redirect('/register')
        
    else:
        return render(request,'login_page.html')

def register_page(request):

    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        if password == confirm:
             user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
             user.save()
             user = auth.authenticate(username=username,password=password)
             if user is not None:
                auth.login(request,user)
                return redirect('home/home')
             else:
                return redirect('register')
        else:
            return redirect('register')
    else:
        return render(request,'register_page.html')



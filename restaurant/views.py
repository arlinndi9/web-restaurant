from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from myapp.models import Contact
from .models import Contact, table,menu



def home(request):
    return render(request, 'index.html')


def Menu(request):
    if 'q' in request.GET:
        q = request.GET['q']
        m=menu.objects.filter(Q(name__icontains=q)|Q(category__icontains=q))
    else:
        m = menu.objects.all()
    context={
        'm':m
    }
    return render(request, 'menu.html',context)

@login_required()
def reservations(request):
    if request.method == "POST":
        name = request.POST.get('name')
        date=request.POST.get('date')
        email=request.POST.get('email')
        time=request.POST.get('time')
        phone=request.POST.get('phone')
        people=request.POST.get('people')
        message=request.POST.get('message')
        reservations = table(name=name, date=date,email=email,time=time,phone=phone,people=people,message=message)
        reservations.save()

    return render(request, 'reservations.html')

@login_required()
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactobj=Contact(name=name,lastname=lastname,email=email,subject=subject,message=message)
        contactobj.save()
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters#
        username = request.POST['username']
        fname = request.POST['fname1']
        lname = request.POST['lname1']
        email = request.POST['email1']
        password1 = request.POST['password2']
        password2 = request.POST['password4']

        # checks for error in filling form
        #validating signupup form
        if len(username)>10:
            messages.error(request,"username must be be under 10 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "username must be contain letters and numbers")
            return redirect('home')

        if password1!=password2:
            messages.error(request, "password doesnt match")
            return redirect('home')

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account is successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 not found')

def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters#
        username = request.POST['username']
        password= request.POST['password6']

        user =authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully loggged in")
            return redirect('home')
        else:
            messages.success(request,'Invalid creditianials')

    return HttpResponse('404 not found')

def handlelogout(request):
    logout(request)
    messages.success(request,"Suucessfully logged out")
    return redirect('home')
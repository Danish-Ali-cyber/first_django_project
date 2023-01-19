from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from .forms import FeedbackForm
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.template import RequestContext

def home(request):
    return render(request,"index.html")

def complaint(request):
    return render(request,"complaint.html")  


def login(request):
    print( request.method)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password)
        print(username,password)
        if user is not None:
            send_mail('Login','U logged in', settings.EMAIL_HOST_USER, [user.email])
            auth_login(request, user)
            return render(request,"dashboard.html")
        else:
            messages.info(request,'username or passowrd is incorrect')
            return render(request,"login.html")
    else:
        return render(request,"login.html")




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in' + username)
            return redirect('login')
                  
    else:
        form = UserRegisterForm()
    
    return render(request,"register.html",{'form': form})      


            

def forgotpassword (request):
    return render(request,"forgotpassword.html")
def dashboard (request):
    return render(request,"dashboard.html")
def academic (request):
    return render(request,"academic.html")
def hostel (request):
    return render(request,"hostel.html")
def mess (request):
    return render(request,"mess.html")

def complaintform1 (request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            send_mail('complaint','complaintss', settings.EMAIL_HOST_USER, ['danishali.321456@gmail.com'])
            form.save()
            return render(request, 'complaintform1.html')
    else:
        form = FeedbackForm()
        return render(request,"complaintform1.html")

def feedback (request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'feedback.html')
    else:
        form = FeedbackForm()
        return render(request,"feedback.html")

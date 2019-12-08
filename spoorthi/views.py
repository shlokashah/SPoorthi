from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import Register
from django.db.models import *


def home(request):
	return render(request,'spoorthi/home.html')

def events(request):
	return render(request,'spoorthi/events.html')

def contact(request):
	return render(request,'spoorthi/contact.html')

def gallery(request):
	return render(request,'spoorthi/gallery.html')

def new(request):
	return render(request,'spoorthi/new.html')

def register(request):
    # return render(request,'blog.html')
    if request.method == 'POST':
        # form = forms.NewsLetterSubscribe(request.POST)
        # if form.is_valid():
        inputEvent = request.POST.get('inputEvent')
        inputName = request.POST.get('inputName')
        inputEmail = request.POST.get('inputEmail')
        inputNumber = request.POST.get('inputNumber')
        inputCollege = request.POST.get('inputCollege')
        inputDescription = request.POST.get('inputDescription')
        form = Register()
        form.event = inputEvent
        form.full_name = inputName
        form.email = inputEmail
        form.number = inputNumber
        form.college = inputCollege
        form.description = inputDescription
        form.save()
        print(form.full_name)
        subject="Successfully Registered For SPoorthi"
        message ="Greetings From Spoorthi SPIT,\nHello "+ form.full_name +",you have succesfully registered for " + form.event+".\nPlease Show this email at the time of Event.\nSee you at SPoorthi from 13-31st January'20.\nSports Team At SPIT"
        from_email=settings.EMAIL_HOST_USER
        to_list=[form.email]
        print(form.email)
        val=send_mail(subject,message,from_email,to_list,fail_silently=False)
        print(val)
        return redirect('register')
    # else:
    # 	form = Register()
    return render(request,'spoorthi/register.html')
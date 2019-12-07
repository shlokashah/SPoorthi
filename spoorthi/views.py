from django.http import HttpResponse
from django.shortcuts import render

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
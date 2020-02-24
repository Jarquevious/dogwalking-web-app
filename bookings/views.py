from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#set up views for pages i need, just show text
def home(request):
    return HttpResponse('home')
def userprofile(request):
    return HttpResponse('userprofile')
def bookings(request):
    return HttpResponse('bookings')

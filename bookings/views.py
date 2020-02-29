from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Booking
from . forms import BookingsForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
#set up views for pages i need, just show text
def home(request):
    return render(request, 'home.html', {})
def userprofile(request):
    return HttpResponse('userprofile')

class BookAWalk(CreateView):
  def get(self, request, *args, **kwargs):
      context = {'form': BookingsForm()}
      return render(request, 'booking.html', context)

  def post(self, request, *args, **kwargs):
      form = BookingsForm(request.POST)
      if form.is_valid():
        booking = form.save()
        return HttpResponseRedirect(reverse_lazy('userprofile'))
      return render(request, 'booking.html', {'form': form})
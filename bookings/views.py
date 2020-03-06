from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Booking
from . forms import BookingsForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import Profile

# Create your views here.
#set up views for pages i need, just show text
def home(request):
    return render(request, 'home.html', {})

class UserProfile(CreateView):
    def get(self, request,*args, **kwargs):   
        # userbookings = Profile.objects.get(request, ) user = get(use)
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user = request.user)
            bookings = Booking.objects.filter(user = request.user)
            context = {'profile':profile, 'bookings': bookings}
            return render(request, 'userprofile.html', context)
        else:
            return redirect('homepage')

        
        

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
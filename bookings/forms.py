from django import forms
from . models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'




    
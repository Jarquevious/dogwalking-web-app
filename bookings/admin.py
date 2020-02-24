from django.contrib import admin
from bookings.models import Dog, Profile, Booking
admin.site.register(Dog)
admin.site.register(Profile)
admin.site.register(Booking)


# Register your models here.
#set up views for pages i need, just show text
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('userprofile/', views.UserProfile.as_view(), name='userprofile'),
    path('booking/', views.BookAWalk.as_view(), name = 'bookings'),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('booking/', views.BookAWalk.as_view(), name = 'bookings'),
]

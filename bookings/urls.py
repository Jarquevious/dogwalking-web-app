from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('userprofile/', views.userprofile),
    path('bookings/', views.bookings),
]

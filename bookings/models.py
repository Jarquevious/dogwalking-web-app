from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True,)
    breed = models.CharField(max_length=30, blank=True, null=True,)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    bio = models.CharField(max_length=30, blank=True, null=True,)
    streetaddress = models.CharField(max_length=30, blank=True, null=True,)
    city = models.CharField(max_length= 30, blank=True, null=True,)
    state = models.CharField(max_length=30, blank=True,null=True,)
    zipcode = models.CharField(max_length=30, blank=True,null=True,)
    phone_number = models.CharField(max_length=30, blank=True,null=True,)
   

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)
    date_time = models.DateTimeField()
    walk_time = models.IntegerField()
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, blank=True, null=True,)

    def __str__(self):
        return self.date_time.strftime('%d-%b-%y') + ' ' + self.user.username
    



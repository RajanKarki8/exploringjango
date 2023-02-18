from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Poet(models.Model):
    headline = models.CharField(max_length=280)
    Description = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    lekhak = models.ForeignKey(User, on_delete= models.CASCADE)
    
    
    def __str__(self):
        return self.headline
    
    def get_absolute_url(self):
        return reverse('poet-create')
    
#class Profile(models.Model):
  #  image=models.OneToOneField()
    

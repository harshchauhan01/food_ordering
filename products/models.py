from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(null=False,blank=False)
    subject=models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Contact Table"

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profiles/%Y/%m/%d',null=True,blank=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
class Order_Food(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=False,blank=False)
    mobile_no=models.TextField()
    numPer=models.TextField(default=1)
    date=models.TextField()
    time=models.TextField()
    table=models.TextField()

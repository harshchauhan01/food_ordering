from django.db import models
import uuid
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
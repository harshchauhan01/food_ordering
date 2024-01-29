from django.contrib import admin
from .models import Contact
# Register your models here.
admin.site.site_header = "Food Zone | Admin"

class Contact_admin(admin.ModelAdmin):
    list_display=['id','name','subject','added_on']
admin.site.register(Contact,Contact_admin)
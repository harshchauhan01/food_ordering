from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request,'index.html')

def contact_page(request):
    context={}
    if request.method=="POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        context['message']=f"Dear {name} , Thanks for visiting"
        
        return redirect("/contact/")

    return render(request,'contact.html',context)

def About(request):
    return render(request,'about.html')

def Feature(request):
    return render(request,'feature.html')

def Menu(request):
    return render(request,'menu.html')

def Chef(request):
    return render(request,'team.html')

def Blog(request):
    return render(request,'blog.html')

def BlogDetail(request):
    return render(request,'single.html')

def Booking(request):
    return render(request,'booking.html')

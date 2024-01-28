from django.shortcuts import render,redirect

# Create your views here.

def Home(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

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

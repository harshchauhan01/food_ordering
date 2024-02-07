from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def Home(request):
    return render(request,'index.html')
@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def About(request):
    return render(request,'about.html')

@login_required(login_url="/login/")
def Feature(request):
    return render(request,'feature.html')

@login_required(login_url="/login/")
def Menu(request):
    return render(request,'menu.html')

@login_required(login_url="/login/")
def Chef(request):
    return render(request,'team.html')

@login_required(login_url="/login/")
def Blog(request):
    return render(request,'blog.html')

@login_required(login_url="/login/")
def BlogDetail(request):
    return render(request,'single.html')

@login_required(login_url="/login/")
def Booking(request):
    context={}
    
    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile_no=request.POST.get("mobile_no")
        numPer=request.POST.get("numPer")
        date=request.POST.get("date")
        time=request.POST.get("time")
        table=request.POST.get("table")
        user = request.user
        Order_Food.objects.create(
            user=user,
            name=name,
            email=email,
            mobile_no=mobile_no,
            numPer=numPer,
            date=date,
            time=time,
            table=table
        )
        
        
        context['message']=f"Dear {name} , Thanks for visiting"

    return render(request,'booking.html',context)


def Register(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User Name already taken')
            return redirect("/register/")
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
            
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect("/register/")

    return render(request,"register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request,user)
                if user.is_superuser or user.is_staff:
                    return redirect('/admin')
                return redirect('/home/')
                
            else:
                messages.info(request,'Invalid Password')
                return redirect('/login/')
            

        else:
            messages.info(request,'Invalid Username')
            return redirect('/login/')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect("/login/")


@login_required(login_url="/login/")
def dashboard(request):
    context={}
    try:
        # Try to get the profile
        profile = Profile.objects.get(user__username=request.user.username)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile.objects.create(user=request.user)
    context['profile']=profile

    if "update-profile" in request.POST:
        name=request.POST.get('name')
        first_name=request.POST.get('first_name')
        profile.user.username=name
        profile.user.first_name=first_name
        profile.user.save()
        
        if "profile_pic" in request.FILES:
            profile_pic=request.FILES.get('profile_pic')
            profile.profile_pic=profile_pic
            profile.save()
        context['status']="Profile updated successfully"
    
    queryset = Order_Food.objects.filter(user=request.user)
    context['orders']=queryset


    return render(request,"dashboard.html",context)
    
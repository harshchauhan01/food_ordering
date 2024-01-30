"""
URL configuration for foodordering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='Home'),
    path('home/',Home,name='Home'),
    path('contact/',contact_page,name='Contact'),
    path('about/',About,name='About'),
    path('feature/',Feature,name='Feature'),
    path('menu/',Menu,name='Menu'),
    path('chef/',Chef,name='Chef'),
    path('blog-grid/',Blog,name='Blog'),
    path('blog-detail/',BlogDetail,name='BlogDetail'),
    path('booking/',Booking,name='Booking'),
    path('register/',Register,name='Register'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
]

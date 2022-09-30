from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request ,"index.html")
    else:
        return redirect("/login")
    
    
    
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request ,"login.html")
    return render(request ,"login.html")
    
def logoutuser(request):
    logout(request)
    return redirect("/login")


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        query=request.POST.get('query')
        country=request.POST.get('country')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        contact=Contact(name=name,email=email,address=address,query=query,country=country,city=city,zip=zip,date=datetime.today())
        contact.save()
        

        
    return  render (request, "contact.html")


def about(request):
    return render(request,"about.html")

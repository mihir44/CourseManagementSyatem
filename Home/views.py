from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db import models

# Maria@20
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login1.html")
    return render(request, 'index.html')


def loginU(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        phone = request.POST.get('phone')
        if password == cpassword:
            user = User(username=username,password=password)
            user.save()
            return render(request, 'login1.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def catalog(request):
    return render(request, 'catalog.html')


def contactus(request):
    return render(request, 'Contactus.html')

def c1(request):
    return render(request, 'c1.html')

def c2(request):
    return render(request, 'c2.html')

def c3(request):
    return render(request, 'c3.html')

def c4(request):
    return render(request, 'c4.html')

def c5(request):
    return render(request, 'c5.html')

def c6(request):
    return render(request, 'c6.html')


def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'catalog.html')
        else:
            return render(request, 'login1.html')

    return render(request, 'login1.html')

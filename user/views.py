from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login as loginsession
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'user/signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User.objects.create_user(username=username, password=password)
        return redirect('/login')
    
def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    elif request.method == "POST":
        return redirect('/home')

@login_required(login_url = '/login')
def home(request):
    if request.method == "GET":
        return render(request, 'user/signup.html')
        
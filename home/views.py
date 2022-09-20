from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,"index.html")

def login_user(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)

    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        return render(request,"login.html")

def logout_user(request):
    logout(request)
    return redirect("/login")

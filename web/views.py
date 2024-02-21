from django.shortcuts import redirect, render
from .models import users
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':

        name = request.POST.get('uname')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        psw2 = request.POST.get('psw2')

        if psw != psw2:
            return redirect ('signup')
        else:
            details = users(uname=name, email=email, psw=psw)
            details.save()

        return redirect('login')

    return render(request, 'signup.html')

def login(request):

    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = authenticate(request, uname=username, psw=password)

        if user is not None:
            login(request, user)
            
            return redirect("dashboard")
        
        else:
            # return redirect('home')
            messages.error(request, 'Invalid username or password.')

    
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

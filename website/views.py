from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Auth views
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("/login")
        else:
            messages.error(request, "An error occured! Please check and try again")
   
    context = {
        "form":form
    }
   
    return render(request, "signup.html", context)

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                user    = authenticate(username=form.data["username"], password=form.data["password"])
                if user:
                    login(request, user)
                    messages.success(request, "Login successful")
                    return redirect('/')
                messages.error(request, "Invalid credentials provided. Note that, both fields may be case-sensitive")
        except Exception as e:
            messages.error(request, "Invalid credentials provided. Note that, both fields may be case-sensitive")
        
        
   
    context = {
        "form":form
    }
    
    return render(request, "registration/login.html", context)

# Main Page
@login_required()
def dashboard(request):
    return render(request, "index.html")

@login_required
def restaurant_view(request):
    return render(request, "restaurant.html")

@login_required
def orders_view(request):
    return render(request, "orders.html")

@login_required
def menu_view(request):
    return render(request, "menu.html")

@login_required
def settings_view(request):
    return render(request, "settings.html")


def logout_view(request):
    logout(request)
    return redirect("/")

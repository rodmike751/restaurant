from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

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


@login_required
def dashboard(request):

    return render(request, "index.html")



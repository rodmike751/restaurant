from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import *
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
def get_cart(request):
    try:
        cart = Order.objects.get(user=request.user, in_cart=True)
    except: 
        cart = []
    return cart

@login_required()
def dashboard(request):
    cart = get_cart(request)
    meals = Meal.objects.all()
    context = {
        "cart":cart,
        "meals":meals
    }

    return render(request, "index.html", context)

@login_required
def restaurant_view(request):
    cart = get_cart(request)
    
    restaurants = Restaurant.objects.all()

    context = {
        "restaurants":restaurants,
        "cart":cart
    }

    return render(request, "restaurant.html", context)

@login_required
def orders_view(request):
    cart = get_cart(request)

    orders = Order.objects.filter(user=request.user, in_cart=False)

    context ={
        "orders":orders,
        "cart":cart
    }
    return render(request, "orders.html", context)

@login_required
def menu_view(request):
    cart = get_cart(request)


    meals = Meal.objects.all()
    context = {
        "meals":meals,
        "cart":cart
    }
    return render(request, "menu.html", context)


@login_required
def menu_detail_view(request, id):
    cart = get_cart(request)
    meal = Meal.objects.get(id=id)
    meals = Meal.objects.filter(category=meal.category)
    context = {
        "meal":meal,
        "meals":meals,
        "cart":cart
    }
    return render(request, "mealDetail.html", context)

# place order
@login_required
def place_order(request, oid):
    order = Order.objects.get(id=oid)
    order.in_cart = False
    order.save()
    messages.success(request, "Order placed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# Add meal to cart
@login_required
def order_meal(request, mid):
    meal = Meal.objects.get(id=mid)
    if Order.objects.filter(user=request.user, in_cart=True).exists():
        Order.objects.get(user=request.user, in_cart=True).meal.add(meal)

    else:
        new_order = Order.objects.create(user=request.user)
        new_order.meal.add(meal)
    messages.success(request, "Added to cart")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def order_remove_meal(request, mid):
    try:
        meal = Meal.objects.get(id=mid)
        Order.objects.get(user=request.user, in_cart=True).meal.remove(meal)
        messages.success(request, "Meal removed from cart")
    except:
        messages.error(request, "Meal not in cart")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def order_switchto_delivered(request, oid):
    order = Order.objects.get(id=oid)
    order.delivered = True 
    order.save()
    messages.success(request, "Order status updated")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def settings_view(request):
    cart = get_cart(request)

    if request.method == 'POST':
        form  = EditUserForm(data= request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successful!")    

    form = EditUserForm(instance=request.user)
    context = {
        "cart":cart,
        "form":form
    }
    return render(request, "settings.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

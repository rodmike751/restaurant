from django.urls import path 
from .import views 

app_name = "website"

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Main pages
    path("", views.dashboard),
    path("restaurants/", views.restaurant_view, name="restaurants"),
    
    path("orders/", views.orders_view, name="orders"),
    path("orders/order/<mid>", views.order_meal, name="order-meal"),
    path("orders/order/delivered/<oid>", views.order_switchto_delivered, name="order-delivered"),
    path("remove/meal/<mid>", views.order_remove_meal, name="remove-meal-from-cart"),
    path("placeorder/<oid>", views.place_order, name="place-order"),

    path("menus/", views.menu_view, name="menus"),
    path("menus/<id>", views.menu_detail_view, name="menus-detail"),


    path("settings/", views.settings_view, name="settings")

]
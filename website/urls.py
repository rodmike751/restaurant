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
    path("menus/", views.menu_view, name="menus"),
    path("settings/", views.settings_view, name="settings")

]
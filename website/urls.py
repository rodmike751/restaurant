from django.urls import path 
from .import views 

app_name = "website"

urlpatterns = [
    path("register", views.register),
    path("", views.dashboard)
]
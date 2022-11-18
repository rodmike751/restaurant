from django.contrib import admin
from .models import Meal, Restaurant, Order 
# Register your models here.
admin.site.site_title = "Resto CPanel"
admin.site.site_header = "Resto CPanel"

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "delivered"]
    list_filter = ["delivered"]


admin.site.register(Meal)
admin.site.register(Restaurant)
admin.site.register(Order, OrderAdmin)
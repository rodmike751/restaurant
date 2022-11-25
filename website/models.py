from django.db import models
from setup.basemodel import TimeBaseModel
from django.contrib.auth.models import User


class Meal(TimeBaseModel):
    MEAL_CHOICE = [
        ("Shawarma", "Shawarma"),
        ("Burgers", "Burgers"),
        ("Charcoal Grilled Chicken", "Charcoal Grilled Chicken"),
        ("Rice", "Rice"),
        ("Salads", "Salads"),
        ("Sandwich", "Sandwich"),
        ("Roasted Chicken", "Roasted Chicken"),
        ("Fried Chicken", "Fried Chicken"),
        ("Drinks", "Drinks"),
        ("Smoothies", "Smoothies"),
        ("Local Dish", "Local Dish")
    ]
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.FloatField(default=0.00)
    description = models.TextField()
    rating = models.IntegerField(default=80)
    category = models.CharField(choices=MEAL_CHOICE, max_length=100)


    def __str__(self):
        return self.name 


class Restaurant(TimeBaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    meals = models.ManyToManyField(Meal, blank=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural = "Restaurant"


class Order(TimeBaseModel):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    meal    = models.ManyToManyField(Meal, blank=True)
    in_cart = models.BooleanField(default=True)
    delivered  = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} ordered {self.meal.name}'

    class Meta:
        verbose_name_plural = "Order"
        ordering = ["-id"]

    @property
    def get_total_price(self):
        total = 0
        for meal in self.meal.all():
            total += meal.price 
        return total
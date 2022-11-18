from django.db import models
from setup.basemodel import TimeBaseModel
from django.contrib.auth.models import User


class Meal(TimeBaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.FloatField(default=0.00)
    description = models.TextField()

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
    delivered  = models.BooleanField(default=False)

    def __str__(self):
        return f'{user.username} ordered {meal.name}'

    class Meta:
        verbose_name_plural = "Order"

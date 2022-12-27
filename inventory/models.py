from django.db import models
from datetime import datetime

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=30)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=30)

    def __str__(self):
        return self.name


class RecipeRequirement(models.Model):
    menu_name = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="requirements")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.menu_name.name + '-' + self.ingredient.name


class Purchase(models.Model):
    menu_name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.menu_name.name + '-' + self.time.strftime("%m/%d/%Y, %H:%M:%S")

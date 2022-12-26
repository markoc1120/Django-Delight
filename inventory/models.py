from django.db import models
import datetime

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=30)
    unit_price = models.FloatField()


class Menuitem(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)


class RecipeRequirement(models.Model):
    menu_name = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Purchase(models.Model):
    menu_name = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.date.today)

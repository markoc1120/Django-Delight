from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'


class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"


class CreateIngredientView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/create_ingredients.html"


class UpdateIngredientView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/update_ingredients.html"


class DeleteIngredientView(DeleteView):
    model = Ingredient
    success_url = "/ingredients"
    template_name = "inventory/delete_ingredients.html"
    name = "delete_ingredients"


class MenuView(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class CreateMenuView(CreateView):
    model = MenuItem
    form_class = MenuForm
    template_name = "inventory/create_menu.html"


class UpdateMenuView(UpdateView):
    model = MenuItem
    form_class = MenuForm
    template_name = "inventory/update_menu.html"


class DeleteMenuView(DeleteView):
    model =MenuItem
    success_url = "/menu"
    template_name = "inventory/delete_menu.html"
    name = "delete_menu"


class RecipeRequirementView(ListView):
    model = RecipeRequirement
    template_name = "inventory/recipereq.html"


class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase.html"

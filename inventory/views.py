from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuForm, RecipeForm, PurchaseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/home.html'
    name = 'home'


class IngredientView(LoginRequiredMixin, ListView):
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


class MenuView(LoginRequiredMixin, ListView):
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


class CreateRecipeView(CreateView):
    model = RecipeRequirement
    form_class = RecipeForm
    template_name = "inventory/create_recipe.html"


class UpdateRecipeView(UpdateView):
    model = RecipeRequirement
    form_class = RecipeForm
    template_name = "inventory/update_recipe.html"


class DeleteRecipeView(DeleteView):
    model =RecipeRequirement
    success_url = "/menu"
    template_name = "inventory/delete_recipe.html"
    name = "delete_recipe"


class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase.html"


def calc_purchase(request):
    purchases = Purchase.objects.all()
    revenue = 0
    expenses = 0

    for purchase in purchases:
        menu_item = purchase.menu_name
        revenue += float(menu_item.price)
        for requirement in menu_item.reciperequirement_set.all():
            expenses += requirement.quantity * float(requirement.ingredient.unit_price)
        profit = float(revenue) - expenses

    context = {
        "revenue": "{:,.2f}".format(round(revenue, 2)),
        "profit": "{:,.2f}".format(round(profit, 2)),
        "expenses": "{:,.2f}".format(round(expenses, 2))
        }
    return render(request, 'inventory/finance.html', context)


class CreatePurchaseView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/create_purchase.html"


class UpdatePurchaseView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/update_purchase.html"


class DeletePurchaseView(DeleteView):
    model =Purchase
    success_url = "/purchase"
    template_name = "inventory/delete_purchase.html"
    name = "delete_purchase"


class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


def logout_request(request):
  logout(request)
  return redirect('home')

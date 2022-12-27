from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuForm, RecipeForm, PurchaseForm
from django.http.response import JsonResponse


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
    template_name = "inventory/recipe.html"


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
    success_url = "/recipe"
    template_name = "inventory/delete_recipe.html"
    name = "delete_recipe"


class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase.html"


def calc_purchase(request):
    purchases = Purchase.objects.all()
    revenue = 0
    expenses = 0

    for purchase in purchases:
        menu_item = purchase.menu_name
        revenue += float(menu_item.price)
        for requirement in menu_item.requirements.all():
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

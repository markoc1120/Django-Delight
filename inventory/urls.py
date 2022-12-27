from django.urls import path
from . import views

urlpatterns = [
  path("", views.HomeView.as_view(), name="home"),
  path("ingredients/", views.IngredientView.as_view(), name='ingredients'),
  path("ingredients/new", views.CreateIngredientView.as_view(), name='create_ingredients'),
  path('ingredients/<pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredients'),
  path('ingredients/<pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredients'),
  path("menu/", views.MenuView.as_view(), name='menu'),
  path("menu/new", views.CreateMenuView.as_view(), name='create_menu'),
  path('menu/<pk>/update', views.UpdateMenuView.as_view(), name='update_menu'),
  path('menu/<pk>/delete', views.DeleteMenuView.as_view(), name='delete_menu'),
  path("recipe/", views.RecipeRequirementView.as_view(), name='recipe'),
  path("recipe/new", views.CreateRecipeView.as_view(), name='create_recipe'),
  path('recipe/<pk>/update', views.UpdateRecipeView.as_view(), name='update_recipe'),
  path('recipe/<pk>/delete', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]

from django.urls import path, include
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
  path("recipe/new", views.CreateRecipeView.as_view(), name='create_recipe'),
  path('recipe/<pk>/update', views.UpdateRecipeView.as_view(), name='update_recipe'),
  path('recipe/<pk>/delete', views.DeleteRecipeView.as_view(), name='delete_recipe'),
  path("purchase/", views.PurchaseView.as_view(), name='purchase'),
  path("purchase/new", views.CreatePurchaseView.as_view(), name='create_purchase'),
  path('purchase/<pk>/update', views.UpdatePurchaseView.as_view(), name='update_purchase'),
  path('purchase/<pk>/delete', views.DeletePurchaseView.as_view(), name='delete_purchase'),
  path('finance/', views.calc_purchase, name='finance'),
  path("account/", include("django.contrib.auth.urls"), name="login"),
  path('signup/', views.SignUp.as_view(), name='signup'),
  path('logout/', views.logout_request, name='logout'),

]

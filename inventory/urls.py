from django.urls import path
from . import views

urlpatterns = [
  path("", views.HomeView.as_view(), name="home"),
  path("ingredients/", views.IngredientView.as_view(), name='ingredients'),
  path("ingredients/new", views.CreateIngredientView.as_view(), name='create_ingredients'),
  path('ingredients/<pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredients'),
  path('ingredients/<pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredients'),
]

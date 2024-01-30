from django.urls import path

from . import views
from .views import add_product_to_recipe, cook_recipe

urlpatterns = [
    path('add_product_to_recipe/', add_product_to_recipe, name='add_product_to_recipe'),
    path('cook_recipe/', cook_recipe, name='cook_recipe'),
    path('show_recipes_without_product/<int:product_id>/', views.show_recipes_without_product, name='show_recipes_without_product'),
]
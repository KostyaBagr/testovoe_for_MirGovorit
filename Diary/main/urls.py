from django.urls import path
from .views import add_product_to_recipe, cook_recipe

urlpatterns = [
    path('add_product_to_recipe/', add_product_to_recipe, name='add_product'),
    path('cook_recipe/', cook_recipe, name='cook_recipe')
]

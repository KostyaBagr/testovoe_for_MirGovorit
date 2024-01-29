from django.urls import path
from .views import add_product_to_recipe

urlpatterns = [
    path('add_product_to_recipe/', add_product_to_recipe, name='add_product')
]
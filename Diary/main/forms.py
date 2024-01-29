
from django import forms

from main.models import ProductIntermediate


class AddProductForm(forms.ModelForm):
    """Форма для добавления продуктов в рецепт"""
    class Meta:
        model = ProductIntermediate
        fields = ["weight", "product", "recipe"]


class CookRecipeForm(forms.Form):
    """Форма для счетчика приготовленных блюд с ипользованием продукта"""
    recipe = forms.CharField(max_length=100)


class ShowRecipesWithoutProductForm(forms.Form):
    """Форма для отображения блюд без данного продукта"""
    product = forms.CharField(max_length=100)
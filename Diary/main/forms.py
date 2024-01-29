
from django.forms import ModelForm

from main.models import ProductIntermediate


class AddProductForm(ModelForm):
    """Форма для добавления продуктов в рецепт"""
    class Meta:
        model = ProductIntermediate
        fields = ["weight", "product", "recipe"]
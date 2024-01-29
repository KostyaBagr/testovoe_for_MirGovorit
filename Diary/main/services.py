from django.shortcuts import render, get_object_or_404
from main.forms import AddProductForm
from main.models import ProductIntermediate, Product, Recipe


def add_product_to_recipe_helper(form: AddProductForm) -> None:
    """Ф-ция для выполнения обработки формы"""
    product = form.cleaned_data['product']
    recipe = form.cleaned_data['recipe']
    weight = form.cleaned_data['weight']

    get_product, get_recipe = get_object_or_404(Product, name=product), get_object_or_404(Recipe, name=recipe)
    productrecipe, _ = ProductIntermediate.objects.get_or_create(product=get_product,
                                                                 recipe=get_recipe)
    productrecipe.weight = weight
    productrecipe.save()


def cook_recipe_helper(recipe: str) ->None:
    """Увеличивает для каждого продукта счетчик на 1"""
    recipe = get_object_or_404(Recipe, id=recipe)
    for r in recipe.products.all():
        r.count += 1
        r.save()


def show_recipes_without_product_helper(product: str) -> None:
    """Фильтр для продуктов, которых нет в рецепте"""



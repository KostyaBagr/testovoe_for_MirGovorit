from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .services import add_product_to_recipe_helper, cook_recipe_helper
# Create your views here.
from main.forms import AddProductForm, CookRecipeForm, ShowRecipesWithoutProductForm
from main.models import Product, Recipe, ProductIntermediate


def add_product_to_recipe(request) -> HttpResponse:
    """Ф-ция для добавления продукта к указанному рецепту"""
    if request.method == 'GET':
        form = AddProductForm(request.GET)
        if form.is_valid():
            add_product_to_recipe_helper(form)
            return HttpResponse(f"Продукт успешно добавлен в рецепт")
    else:
        form = AddProductForm()

    all_products, all_recipes = Product.objects.all(), Recipe.objects.all()

    return render(request, 'main/add_product_to_recipe.html',
                  {'form': form, 'products': all_products, 'recipes': all_recipes})


def cook_recipe(request):
    """Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт"""
    if request.method == "GET":
        form = CookRecipeForm(request.GET)
        if form.is_valid():
            recipe = form.cleaned_data['recipe']
            cook_recipe_helper(recipe)
            return HttpResponse(f'Счетчик для каждого продукта в рецепте {recipe} увеличился на 1')
    else:
        form =CookRecipeForm()

    all_recipes = Recipe.objects.all()
    return render(request, "main/cook_recipe.html", {"form": form, "recipes": all_recipes})


def show_recipes_without_product(request):
    """Ф-ция возвращает рецепты, где данного продукта нет или меньше 10 грм"""
    if request.method == "GET":
        form = ShowRecipesWithoutProductForm(request.GET)
        if form.is_valid():
            product = form.cleaned_data['product']
            print(product)
            recipes = Recipe.objects.exclude(productintermediate__product=product) \
                .filter(productintermediate__weight__lt=10)

            context = {
                'recipes': recipes,
                'product_id': product,
            }
            print(recipes, 'рецепты')
            return render(request, 'main/show_recipes_without_product.html', context)
    else:
        form = ShowRecipesWithoutProductForm()
    all_products = Product.objects.all()
    return render(request, 'main/show_recipes_without_product_form.html', {'form': form, 'products': all_products})
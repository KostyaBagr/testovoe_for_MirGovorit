from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.forms import AddProductForm
from main.models import Product, Recipe, ProductIntermediate


def add_product_to_recipe(request):
    """Ф-ция для добавления продукта к указанному рецепту"""
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            recipe = form.cleaned_data['recipe']
            weight = form.cleaned_data['weight']

            get_product, get_recipe = get_object_or_404(Product, name=product), get_object_or_404(Recipe, name=recipe)
            productrecipe, _ = ProductIntermediate.objects.get_or_create(product=get_product,
                                                                      recipe=get_recipe)
            productrecipe.weight = weight
            productrecipe.save()


            return HttpResponse(f"Продукт {product} успешно добавлен в рецепт {recipe}")
    else:
        form = AddProductForm()

    all_products, all_recipes = Product.objects.all(), Recipe.objects.all()

    return render(request, 'main/add_product_to_recipe.html',
                  {'form': form, 'products': all_products, 'recipes': all_recipes})

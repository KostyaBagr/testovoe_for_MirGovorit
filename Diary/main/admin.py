from django.contrib import admin
from .models import Recipe,Product, ProductIntermediate
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(ProductIntermediate)
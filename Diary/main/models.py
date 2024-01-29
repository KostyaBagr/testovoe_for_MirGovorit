from django.db import models


# Create your models here.
class Product(models.Model):
    """Хранит информацию о продукте"""
    name = models.CharField(verbose_name='Название', max_length=100)
    count = models.IntegerField('Кол-во приготовления блюда', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Хранит рецепт блюда"""
    name = models.CharField('Название', max_length=100)
    products = models.ManyToManyField(Product, through='ProductIntermediate')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class ProductIntermediate(models.Model):
    """Промежуточная модель для хранения блюд"""

    weight = models.IntegerField("Вес (грм)", default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')



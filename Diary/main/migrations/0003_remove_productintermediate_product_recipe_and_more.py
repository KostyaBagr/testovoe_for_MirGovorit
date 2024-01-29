# Generated by Django 5.0.1 on 2024-01-29 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productintermediate',
            name='product_recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='intermediate_product',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='product',
        ),
        migrations.AddField(
            model_name='productintermediate',
            name='Recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productintermediate',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(through='main.ProductIntermediate', to='main.product'),
        ),
        migrations.AlterField(
            model_name='productintermediate',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Вес (грм)'),
        ),
    ]
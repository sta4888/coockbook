from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        if recipe_id and product_id and weight:
            recipe = get_object_or_404(Recipe, pk=int(recipe_id))
            product = get_object_or_404(Product, pk=int(product_id))

            recipe_product = RecipeProduct.objects.filter(recipe=recipe, product=product).first()

            if recipe_product:
                recipe_product.weight = int(weight)
                recipe_product.save()

                return JsonResponse({'message': f'Product weight updated to {weight} grams.'})
            else:
                recipe_product = RecipeProduct(recipe=recipe, product=product, weight=int(weight))
                recipe_product.save()

                return JsonResponse({'message': f'Product added to recipe with weight {weight} grams.'})
        else:
            return JsonResponse({'error': 'Missing parameters.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')

        if recipe_id:
            try:
                recipe = get_object_or_404(Recipe, pk=recipe_id)

                recipe_products = RecipeProduct.objects.filter(recipe=recipe)

                for recipe_product in recipe_products:
                    product = recipe_product.product
                    product.times_cooked += 1
                    product.save()

                return JsonResponse({'message': f'Recipe {recipe.name} cooked successfully.'})
            except Recipe.DoesNotExist:
                return JsonResponse({'error': 'Recipe does not exist.'}, status=404)
        else:
            return JsonResponse({'error': 'Missing parameter "recipe_id".'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    recipes = Recipe.objects.exclude(recipeproduct__product=product) \
                             .prefetch_related('recipeproduct_set') \
                             .filter(recipeproduct__weight__lt=10)

    return render(request, 'cookbook/recipes_without_product.html', {'recipes': recipes, 'product': product})
from django.shortcuts import render
from .models import Product


def all_products(request):
    """A View to display all items"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

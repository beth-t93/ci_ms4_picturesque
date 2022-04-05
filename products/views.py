from django.shortcuts import get_object_or_404, render
from .models import Product


def all_products(request):
    """A view to display all items"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products.html', context)

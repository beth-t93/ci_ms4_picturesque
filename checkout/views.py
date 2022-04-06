from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing here at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KOTyFE1zig55cHiLe5KSTyyfmMhHslnmXeEWaoW6GtK6WNyfN7nR7LAtELiuTuFNaVZziL5lExPPQRGkuzd5tDS00sx0vUDDm',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
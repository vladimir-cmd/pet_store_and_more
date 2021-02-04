from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('product'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IHDzPLhMGhoweMgmkDmCxFwpuxmLma5PpmbnIIVMAa7nqZjIe72FYGKQkkofPjy91h17SbQO7D1NvocIUCNdThk00qIURxA0N',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

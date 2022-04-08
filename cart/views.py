from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .carts import Cart
from store.models import Product
from .forms import AddCartForm


@login_required(login_url='login')
def cart_view(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = AddCartForm(
            initial={
                "update": True,
            }
        )
    return render(request, 'cart/cart.html', context={"cart": cart})


@login_required(login_url='login')
@require_POST
def add_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    form = AddCartForm(request.POST)
    if form.is_valid():
        info = form.cleaned_data
        cart.add(
            product=product,
            quantity=info['quantity'],
            update_quantity=info['update']
        )
    return redirect('cart-view')


@login_required(login_url='login')
@require_POST
def remove_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    cart.remove(
        product=product
    )
    return redirect('cart-view')

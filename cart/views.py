from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from cart.carts import _session_id
from cart.models import Cart, CartItem
from store.models import Product
from order.models import Orders


@login_required(login_url='login')
def cart_view(request):
    order = Orders.objects.filter(user=request.user).exists()
    all_items = CartItem.objects.filter(cart_user=request.user)
    total = 0
    for i in all_items:
        total += (i.cart_product.price * i.quantity)

    return render(request, 'cart/cart.html', context={'items': all_items, 'total': total, 'order': order})


def add_cart(request, pk):
    logged_user = request.user
    product = Product.objects.get(id=pk)
    try:
        cart = Cart.objects.get(cart_id=_session_id(request))
    except ObjectDoesNotExist:
        cart = Cart.objects.create(
            cart_id=_session_id(request)
        )
        cart.save()
    item_is_exists = CartItem.objects.filter(cart_user=logged_user, cart_product=product).exists()
    if item_is_exists:
        cart_item = CartItem.objects.get(cart_user=logged_user, cart_product=product)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(
            cart_product=product,
            cart_user=logged_user,
            cart=cart,
            quantity=1
        )
    cart_item.save()
    return redirect('cart-view')


def remove_cart(request, pk):
    logged_user = request.user
    product = get_object_or_404(Product, id=pk)
    cart_item = CartItem.objects.get(cart_product=product, cart_user=logged_user, )
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('cart-view')
    else:
        cart_item.delete()
        return redirect('cart-view')

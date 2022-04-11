from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Address, Order
from .forms import OrderForm
from cart.carts import Cart
from django.contrib import messages


@login_required(login_url='login')
def add_order(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(request.POST)
        description = request.POST['description']
        if form.is_valid():
            info = form.cleaned_data
            address_info = Address.objects.create(
                user=request.user,
                address_user=info['address_user'],
                country=info['country'],
                postal_code=info['postal_code'],
                description=description,
            )
            for item in cart:
                Order.objects.create(
                    order_info=address_info,
                    product=item['product'],
                    order_price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

        messages.success(request, 'Your order has been processed')
        return redirect('home')

    context = {
        'address_form': OrderForm(),
    }
    return render(request, 'cart/checkout.html', context)


def contact(request):
    return render(request, 'cart/contact.html')

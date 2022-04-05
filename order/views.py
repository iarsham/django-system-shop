from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Orders
from .forms import OrderForm
from django.contrib import messages


@login_required(login_url='login')
def add_order(request):
    all_items = CartItem.objects.filter(cart_user=request.user)
    total = 0
    for i in all_items:
        total += (i.cart_product.price * i.quantity)
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            description = request.POST['description']
            Orders.objects.create(
                user=request.user,
                address=info['address'],
                city=info['city'],
                country=info['country'],
                postal_code=info['postal_code'],
                description=description
            )

            messages.success(request, 'Your order has been processed')
            return redirect('home')
        else:
            messages.warning(request, "Error happened!")
    context = {
        'address_form': OrderForm(),
        'total': total,
    }
    return render(request, 'cart/checkout.html', context)


def contact(request):
    return render(request, 'cart/contact.html')

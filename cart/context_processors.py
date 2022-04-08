from .carts import Cart


def _id_cart(request):
    return {'cart': Cart(request)}

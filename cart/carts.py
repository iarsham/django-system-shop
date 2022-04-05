def _session_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

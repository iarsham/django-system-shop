from django.shortcuts import render, redirect
from .models import Product, Comment
from .utils import paginate, run_filter
from cart.forms import AddCartForm
from django.contrib import messages


def category(request):
    q = request.GET.get('q') or request.GET.get('sort') or request.GET.get('search')
    if q:
        query = run_filter(request)
    else:
        query = paginate(request)

    context = {
        'products': query,
        'cart_form': AddCartForm()
    }
    return render(request, 'store/category.html', context)


def product_detail(request, pk):
    project_detail = Product.objects.get(id=pk)
    product_comments = Comment.objects.all()
    if request.method == "POST":
        if request.user.is_authenticated:
            query = request.POST['comment']
            comment = Comment.objects.create(
                text_comment=query,
                reply_product=project_detail,
                writer=request.user
            )
        else:
            messages.warning(request, 'Please Login To send comment ')
            return redirect('login')

    context = {
        'project_detail': project_detail,
        'product_comments': product_comments,
        'cart_form': AddCartForm()
    }
    return render(request, 'store/product_detail.html', context)

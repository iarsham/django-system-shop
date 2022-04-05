from django.shortcuts import render
from .models import Product, Comment
from .utils import paginate, run_filter


def category(request):
    if 'q' or 'search' or 'sort' in request.GET:
        query = run_filter(request)
    else:
        query = paginate(request)

    context = {
        'products': query,
    }
    return render(request, 'store/category.html', context)


def product_detail(request, pk):
    project_detail = Product.objects.get(id=pk)
    product_comments = Comment.objects.all()
    if request.method == "POST":
        query = request.POST['comment']
        comment = Comment.objects.create(
            text_comment=query,
            reply_product=project_detail,
            writer=request.user
        )
        comment.save()

    context = {
        'project_detail': project_detail,
        'product_comments': product_comments,
    }
    return render(request, 'store/product_detail.html', context)
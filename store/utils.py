from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def run_filter(request):
    if 'search' in request.GET:
        search = request.GET.get('search')
        query = Product.objects.filter(
            Q(product_name__icontains=search) |
            Q(product_brand__icontains=search)
        ).distinct()
        return query

    elif 'q' in request.GET:
        q = request.GET.get('q')
        query = Product.objects.filter(
            Q(category__slug__icontains=q) |
            Q(screen__icontains=q) |
            Q(product_brand__icontains=q)
        ).distinct()
        return query

    else:
        s = request.GET.get('sort')
        if s == 'high':
            query = Product.objects.order_by('-price')
        elif s == "new":
            query = Product.objects.order_by('-added_date')
        else:
            query = Product.objects.order_by('price')
        return query


def paginate(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        query = paginator.page(1)
    except EmptyPage:
        query = paginator.page(paginator.num_pages)
    return query

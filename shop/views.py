from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'shop/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product
    }

    return render(request, 'shop/product_detail.html', context)

def product_search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'query': query,
        'results': results
    }
    return render(request, 'shop/search_results.html', context)
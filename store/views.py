from django.shortcuts import render
from .models import Product, Category

def store_view(request):
    # Fetch all active products
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    
    # Check for category filter in URL (?category=slug)
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
    }
    return render(request, 'store.html', context)
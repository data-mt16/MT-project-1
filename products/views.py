from django.shortcuts import render
from .models import Product

# This function will be our product list page
def product_list_view(request):
    # 1. Get all products from the database
    all_products = Product.objects.all()

    # 2. Prepare the data to send to the template
    context = {
        'products': all_products
    }

    # 3. Render the HTML page and send the data to it
    return render(request, 'products/product_list.html', context)
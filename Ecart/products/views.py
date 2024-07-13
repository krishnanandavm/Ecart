from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render (request, 'index.html')

def list_products(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_

    Return:
        _type_:_description_        
    """
   
    product_list = Product.objects.all()
    product_paginator = Paginator(product_list, 2)
    # Get the page number from the request, default to 1 if not provided
    page = request.GET.get('page', 1)
    product_list = product_paginator.get_page(page)
    context = {'products': product_list}
    return render (request, 'products.html',context)

def detail_product(request):
    if request.POST:
        print(request.POST)
    return render (request, 'product_details.html')
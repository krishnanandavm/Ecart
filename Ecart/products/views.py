from django.shortcuts import render
from . models import Product
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
    context = {'products': product_list}
    return render (request, 'products.html',context)

def detail_product(request):
    if request.POST:
        print(request.POST)
    return render (request, 'product_details.html')
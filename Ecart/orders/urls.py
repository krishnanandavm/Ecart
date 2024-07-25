
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('cart', views.show_cart,name='cart'),
    path('add_to_cart', views.add_to_cart,name='add_to_cart'),


]

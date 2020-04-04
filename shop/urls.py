from django.urls import path
from .views import *



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page_id>', ShopView.as_view()),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-single/', BlogSingleView.as_view(), name='blog-single'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product-single/', ProductSingleView.as_view(), name='product-single'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),

]

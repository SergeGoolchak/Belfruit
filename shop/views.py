
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .settings.base import *
from django.core.paginator import Paginator
from shop.models import *


# Create your views here.

class IndexView(View):

    def get(self, request):
    
        for k, v in request.COOKIES.items():
            print(k, v)
    
        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                   'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                   'description': DESCRIPTION, 'address': ADDRESS,
                                                   'tech_phone_number': TECH_PHONE_NUMBER})

class ShopView(View):

    def get(self, request, page_id=1):    
    
        products_list = [{'name':       'Bell Pepper',
                     'image':      'shop/images/product-1.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'}, 
                    {'name':       'Strawberry',
                     'image':      'shop/images/product-2.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Green Beans',
                     'image':      'shop/images/product-3.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Purple Cabbage',
                     'image':      'shop/images/product-4.jpg',
                     'price':      '$120.00'},
                    {'name':       'Tomatoe',
                     'image':      'shop/images/product-5.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},   
                    {'name':       'Brocolli',
                     'image':      'shop/images/product-6.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Carrots',
                     'image':      'shop/images/product-7.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Fruit Juice',
                     'image':      'shop/images/product-8.jpg',
                     'price':      '$120.00'},     
                    {'name':       'Onion',
                     'image':      'shop/images/product-9.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},    
                    {'name':       'Apple',
                     'image':      'shop/images/product-10.jpg',
                     'price':      '$120.00'},   
                    {'name':       'Garlic',
                     'image':      'shop/images/product-11.jpg',
                     'price':      '$120.00'},     
                    {'name':       'Chilli',
                     'image':      'shop/images/product-12.jpg',
                     'price':      '$120.00'}]

        for i in products_list:
            p = Product(name=i['name'], image=i['image'], price=i['price'])
            if 'discount' in i:
                p.discount = i['discount']
                p.price_sale = i['price_sale']
            p.save()

        products_list = []
        for i in Product.objects.all():
            p = dict(name=i.name, image=i.image, price=i.price)
            if i.discount:
                p['discount'] = i.discount
                p['price_sale'] = i.price_sale
            products_list.append(p)
        print(products_list)

        #     # products_list.append(new_product)

        paginator = Paginator(products_list, 4)
        
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))
            
        return render(request, 'shop/shop.html', {'products': products, 'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                   'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                   'description': DESCRIPTION, 'address': ADDRESS,
                                                   'tech_phone_number': TECH_PHONE_NUMBER})


class ContactView(View):

    def get(self, request):
        return render(request, 'shop/contact.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                   'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                   'description': DESCRIPTION, 'address': ADDRESS,
                                                   'tech_phone_number': TECH_PHONE_NUMBER})
        
        
class AboutView(View):

    def get(self, request):
        return render(request, 'shop/about.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                   'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                   'description': DESCRIPTION, 'address': ADDRESS,
                                                   'tech_phone_number': TECH_PHONE_NUMBER})
        
        
class BlogView(View):

    def get(self, request):
        blogs = [{'date': 'July 20, 2019',
                 'image': '/static/shop/images/image_1.jpg',
                 'author': 'Admin',
                 'comment_number': '3',
                 'header': 'Even the all-powerful Pointing has no control about the blind texts',
                 'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
                {'date': 'July 25, 2019',
                 'image': '/static/shop/images/image_2.jpg',
                 'author': 'User1',
                 'comment_number': '5',
                 'header': 'Even the all-powerful Pointing has no control about the blind texts',
                 'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
                {'date': 'August 22, 2019',
                 'image': '/static/shop/images/image_3.jpg',
                 'author': 'User2',
                 'comment_number': '6',
                 'header': 'Even the all-powerful Pointing has no control about the blind texts',
                 'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
                {'date': 'June 11, 2019',
                 'image': '/static/shop/images/image_4.jpg',
                 'author': 'User3',
                 'comment_number': '2',
                 'header': 'Even the all-powerful Pointing has no control about the blind texts',
                 'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
                {'date': 'May 02, 2019',
                 'image': '/static/shop/images/image_5.jpg',
                 'author': 'Sam F.',
                 'comment_number': '1',
                 'header': 'Even the all-powerful Pointing has no control about the blind texts',
                 'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
                {'date': 'September 01, 2019',
                 'image': '/static/shop/images/image_6.jpg',
                 'author': 'Ur Mom',
                 'comment_number': '7',
                 'header': 'Even the all-powerful Pointing has no control about the blind texts',
                 'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'}
                ]

        return render(request, 'shop/blog.html', {'blogs': blogs, 'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                   'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                   'description': DESCRIPTION, 'address': ADDRESS,
                                                   'tech_phone_number': TECH_PHONE_NUMBER})




class BlogSingleView(View):

    def get(self, request):
        return render(request, 'shop/blog-single.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                  'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                  'description': DESCRIPTION, 'address': ADDRESS,
                                                  'tech_phone_number': TECH_PHONE_NUMBER})


class CartView(View):

    def get(self, request):
        products = [{'name': 'Bell Pepper',
                     'image': '/static/shop/images/product-3.jpg',
                     'price': '$4.90',
                     'total': '$4.90',
                     'description': 'Far far away, behind the word mountains, far from the countries',
                     'value': '1',
                     'min': '$1',
                     'max': '100'},
                    {'name': 'Bell Pepper',
                     'image': '/static/shop/images/product-4.jpg',
                     'price': '$15.70',
                     'total': '$15.70',
                     'description': 'Far far away, behind the word mountains, far from the countries',
                     'value': '1',
                     'min': '$1',
                     'max': '100'}]

        return render(request, 'shop/cart.html', {'products': products, 'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                         'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                         'description': DESCRIPTION, 'address': ADDRESS,
                                                         'tech_phone_number': TECH_PHONE_NUMBER})


class CheckoutView(View):

    def get(self, request):
        return render(request, 'shop/checkout.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                      'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                      'description': DESCRIPTION, 'address': ADDRESS,
                                                      'tech_phone_number': TECH_PHONE_NUMBER})


class ProductSingleView(View):

    def get(self, request):
        return render(request, 'shop/product-single.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                            'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                            'description': DESCRIPTION, 'address': ADDRESS,
                                                            'tech_phone_number': TECH_PHONE_NUMBER})


class WishlistView(View):

    def get(self, request):
        return render(request, 'shop/wishlist.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                      'delivery': DELIVERY, 'business_name': BUSINESS_NAME,
                                                      'description': DESCRIPTION, 'address': ADDRESS,
                                                      'tech_phone_number': TECH_PHONE_NUMBER})

        
        
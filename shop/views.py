from django.shortcuts import redirect,render,get_object_or_404
from shop.models import *
# Create your views here.
def home(request):
    Products=Product.objects.all()
    return render (request,'home.html',context={'Products':Products} )


def product_detail(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    return render (request,'product_detail.html',context={'product':product} )




def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    for product in products:
        quantity = cart.get(str(product.id), 0)
        cart_items.append({
            'product': product,
            'quantity': quantity,
        })

    return render(request, 'cart.html', context={'cart_items': cart_items})

def displaycart(request):
    cart=request.session.get('cart',{})
    product_ids = cart.keys()  # Get all keys from the session cart
   
    products = Product.objects.filter(id__in=product_ids)
    cart_items=[]
    grandtotal=0
    for product in products:
        quantity=cart.get(str(product.id),0)
        total=product.price*quantity
        grandtotal+=total
        cart_items.append({
            'product':product,
            'quantity':quantity,
             'total': total,
             
        })

    return render (request,'cart.html',context={'cart_items':cart_items, 'grandtotal': grandtotal} )

def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    return redirect('displaycart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]  # Remove product if quantity becomes 0

    request.session['cart'] = cart
    return redirect('displaycart')

def remove(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
         del cart[product_id]
        
       # Remove product if quantity becomes 0

    request.session['cart'] = cart
    return redirect('displaycart')


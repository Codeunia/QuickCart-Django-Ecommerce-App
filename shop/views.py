from django.shortcuts import redirect,render,get_object_or_404
from shop.models import *
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CustomerRegistrationForm,CustomerLoginForm,CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
# Create your views here.
def home(request):
    Products=Product.objects.all()
    return render (request,'home.html',context={'Products':Products} )


def product_detail(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    return render (request,'product_detail.html',context={'product':product} )

def order_confirmation(request, order_id):
    return render(request, 'order_confirmation.html', {'order_id': order_id})



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
    product_ids = [int(pid) for pid in cart.keys()]# Get all keys from the session cart
   
    products = Product.objects.filter(id__in=product_ids)
    cart_items=[]
    grandtotal=0
    for product in products:
        quantity=cart.get(str(product.id),0)
        total=product.price*quantity
        
        cart_items.append({
            'product':product,
            'quantity':quantity,
             'total': total,
             
        })
        grandtotal+=total

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
# def checkout(request)
@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')  # or wherever your cart view is

    customer, created = Customer.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Optional: Allow user to update their address during checkout
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()

            with transaction.atomic():
                order = Order.objects.create(customer=customer)

                total_amount = 0

                for product_id, quantity in cart.items():
                    try:
                        product = Product.objects.get(id=product_id)
                        subtotal = product.price * quantity

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                            price_at_order_time=product.price,
                        )

                        total_amount += subtotal
                    except Product.DoesNotExist:
                        messages.warning(request, f"Product with ID {product_id} no longer exists.")
                        continue

                if total_amount == 0:
                    messages.error(request, "No valid products found in cart.")
                    return redirect('cart')

                order.total_amount = total_amount
                order.save()

                # Clear cart
                request.session['cart'] = {}
                request.session.modified = True

                return redirect('order_confirmation', order_id=order.id)
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'checkout.html', {
        'form': form,
        'cart': cart,
    })


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)  # ⬅️ removed 'request='
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')  # change this
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomerLoginForm()
    return render(request, 'login.html', {'form': form})
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)  # ⬅️ removed 'request='
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('checkout')  # change this
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomerLoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    # messages.success(request, "You have been logged out.")
    return redirect('home')
def register_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
                
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, 'register.html')
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            customer=Customer.objects.create(
                user=user,
                email=email,
                phone=phone,
                address=address
                
            )
            # user.set_password(password)
            
            messages.info(request, "Registration successful!")
            return redirect('/login/')
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = CustomerRegistrationForm()
    
    return render(request,'register.html',{'form':form})
        
          
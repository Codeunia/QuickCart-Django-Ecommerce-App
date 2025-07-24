from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:product_id>/', views.remove, name='remove'),

    path('displaycart/', views.displaycart, name='displaycart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),

path('logout/', views.logout_view, name='logout'),
]
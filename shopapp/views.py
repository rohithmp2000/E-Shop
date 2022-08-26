from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from shopapp.forms import LoginRegister, SellerRegister, UserRegister
# from vaccination_app.forms import UserRegister, NurseRegister, LoginRegister

from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Products.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def payment(request):
	return render(request, 'store/payment.html')

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.user
	product = Products.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.User
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
# -------------------
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_seller:
                return redirect('seller_home')
            elif user.is_user:
                return redirect('user_home')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def select_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'Seller':
            return redirect('seller_register')
        elif role == 'User':
            return redirect('user_register')

        else:
            messages.info(request, 'Please Choose a Role')

    return render(request, 'select_role.html')


def seller_register(request):
    user_form = LoginRegister()
    seller_form = SellerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        seller_form = SellerRegister(request.POST)
        if user_form.is_valid() and seller_form.is_valid():
            user = user_form.save(commit=False)
            user.is_seller = True
            user.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            seller.save()
            messages.info(request, 'Seller Registered Successfully')
            return redirect('login_view')
    return render(request, 'seller_registration.html', {'user_form': user_form, 'seller_form': seller_form})


def user_register(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            c = user_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, 'User Registered Successfully')
            return redirect('login_view')
    return render(request, 'user_registration.html', {'login_form': login_form, 'user_form': user_form})


def logout_view(request):
    logout(request)
    return redirect('login_view')

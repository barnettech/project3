from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Food, Order, Order_Number
from .forms import OrderFoodForm
import datetime

# Create your views here.
def index(request):
    if request.user.username is not None:
      return redirect('order')
    return render(request, 'index.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('order')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def menu(request):
    #return render(request, 'menu.html', {})
    food_list=Food.objects.all()
    food_count=Food.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'menu.html',
        context={'food_list':food_list, 'food_count':food_count},
    )

def order_from_menu(request):
    food_list=Food.objects.all()
    shopping_cart_food = {};
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        ON = Order_Number()
        ON.save()
        for i in range(0,len(food_list)):
            data = request.POST.get('fooditem_' + str(i))
            if data:
                food = Food.objects.get(pk=i)
                persons_name = request.user.first_name + request.user.last_name
                O = Order(title=food, username=request.user.username, name=persons_name, phone='888-777-7777', price='9.98', size='Large', food_type='PIZZA', order_number = ON)
                O.save()
                #shopping_cart_food[food.title] = data

    shopping_cart_food = Order.objects.filter(username=request.user.username, order_status='INCOMPLETE')
    print(shopping_cart_food)
    cart_count = Order.objects.filter(username=request.user.username, order_status='INCOMPLETE').count()
    print(cart_count)
    if cart_count < 1:
        shopping_cart_food = 'Empty Cart'

    return render(request, 'order_food_form.html', {'food_list':food_list, 'shopping_cart_food':shopping_cart_food})

def checkout(request):
    shopping_cart = Order.objects.filter(username=request.user.username, order_status='INCOMPLETE').update(order_status='FILLED')
    return render(request, 'thankyou.html', {'checkedout':1})
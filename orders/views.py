from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Food
from .forms import OrderFoodForm
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def signup(request):
    print('here')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
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
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = OrderFoodForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            food_list.name = form.cleaned_data['renewal_date']
            food_list.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('menu') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = OrderFoodForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'order_food_form.html', {'form': form, 'bookinst':food_list})
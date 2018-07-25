from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food

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
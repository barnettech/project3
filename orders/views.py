from django.http import HttpResponse
from django.shortcuts import render
from .models import Food

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

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

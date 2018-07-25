from django.urls import path
from .models import Food

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    #path('menu-items/', views.FoodListView.as_view(), name='foods'),
]

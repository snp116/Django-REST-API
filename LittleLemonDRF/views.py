from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.response import Response
from .models import MenuItem, Category, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework import status, generics
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    
    serializer_class = MenuItemSerializer
    
    def get_queryset(self):
        menu_items = MenuItem.objects.all()
        return menu_items

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
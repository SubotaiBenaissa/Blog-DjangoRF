from django.shortcuts import render
from requests import request
from rest_framework.viewsets import ModelViewSet
from .models import Category
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly
# Create your views here.

class CategoryViewSet(ModelViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']
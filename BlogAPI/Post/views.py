from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Post.models import Post
from .serializers import PostSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PostApiViewSet(ModelViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
    

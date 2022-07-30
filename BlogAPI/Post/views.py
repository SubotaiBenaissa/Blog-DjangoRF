from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Post.models import Post
from .serializers import PostSerializer
# Create your views here.

class PostApiViewSet(ModelViewSet):
    
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
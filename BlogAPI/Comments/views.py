from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsOwnerOrReadAndCreateOnly
# Create your views here.

class CommentApiViewSet(ModelViewSet):
    
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['post']
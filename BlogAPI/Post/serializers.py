from rest_framework import serializers
from Post.models import Post
from Users.serializers import UserSerializer
from Categories.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    category = CategorySerializer()
    
    class Meta:
        
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
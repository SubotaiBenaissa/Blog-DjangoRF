from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.db.models import SET_NULL
from Users.models import User
from Categories.models import Category
# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length = 255)
    content = models.TextField()
    slug = models.SlugField(max_length = 255, unique = True)
    miniature = models.ImageField(upload_to = 'Post/imgs/')
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = SET_NULL, null = True)
    category = models.ForeignKey(Category, on_delete = SET_NULL, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    class Meta: 
        
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        
        return self.title 
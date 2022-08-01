from django.db import models
from django.db.models import CASCADE
from Users.models import User
from Post.models import Post

# Create your models here.

class Comment(models.Model):
    
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = CASCADE, null = False)
    post = models.ForeignKey(Post, on_delete = CASCADE, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    class Meta: 
        
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        
        return self.content
from django.db import models
from django.contrib.auth.models import User
from posts.models import BlogPost

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    post = models.ForeignKey(BlogPost, null=False, blank=False, on_delete=models.CASCADE)

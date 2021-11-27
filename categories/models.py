from django.db import models

# Local models
from posts.models import BlogPost

class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7)
    posts = models.ManyToManyField(BlogPost)

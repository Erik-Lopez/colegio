from django.db import models

from django.contrib.auth.models import User
from posts.models import BlogPost

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, null=False, blank=False, on_delete=models.CASCADE, default=BlogPost.objects.get(pk=1).pk)
    content = models.TextField()

    parent_comment = models.ForeignKey('self', default=None, null=True, blank=False, on_delete=models.DO_NOTHING)
    posted_at = models.DateTimeField(auto_now_add=True)

# Python
from enum import Enum

# Django
from django.db import models

# Create your models here.

class User(models.Model):
    pass

class Club(models.Model):
    pass

class Tag(Enum):
    TAG1 = 1
    TAG2 = auto()

class BlogPost(models.Model):
#    post_id

    title = models.CharField(max_length=30)
    content = models.TextField()

    author_id = models.ForeignKey(User, on_delete=models.SET_NULL)
#    tags_id   = models.ForeignKey(Tag, on_delete=models.SET_NULL)
    club_id   = models.ForeignKey(Club, on_delete=models.SET_NULL)

    posted_at = models.Date

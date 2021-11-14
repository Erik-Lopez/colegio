# Python
from enum import Enum, auto

# Django
from django.db import models
from users.models import User

# Create your models here.
class Club(models.Model):
    pass

class Tag(Enum):
    TAG1 = 1
    TAG2 = auto()

class BlogPost(models.Model):
#    post_id

    title = models.CharField(max_length=30)
    content = models.TextField()

    author_id = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
#    tags_id   = models.ForeignKey(Tag, on_delete=models.SET_NULL)
    club_id   = models.ForeignKey(Club, null=True, blank=True, on_delete=models.SET_NULL)

    posted_at = models.DateTimeField(auto_now_add=True)

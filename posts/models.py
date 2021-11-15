# Python
from enum import Enum, auto

# Django
from django.db import models
from users.models import User
from clubs.models import Club

# Create your models here.

#class Tag(Enum):
#    TAG1 = 1
#    TAG2 = auto()

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    description = models.CharField(max_length=60)

    author_id = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
#    tags_id   = models.ForeignKey(Tag, on_delete=models.SET_NULL)
    club_id   = models.ForeignKey(Club, null=True, blank=True, on_delete=models.SET_NULL)

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

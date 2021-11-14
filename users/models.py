from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #clubs

    profile_pic = models.ImageField(upload_to="users/profile_pics", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username



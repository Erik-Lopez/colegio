from django.db import models

# Local models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=240)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="clubs/logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='User (Default)', max_length=200, null=True)
    title = models.CharField(default="Please give your name and other info from the below 'Edit' option.", max_length=200, null=True)
    desc_text = 'Hey there, nice to meet you.'
    desc = models.CharField(default = desc_text, max_length=200, null=True)
    profile_img = models.ImageField(default='media/default.jpg', upload_to='media', null='True', blank=True)


    def __str__(self):
        return f"{self.user.username}'s profile"
    

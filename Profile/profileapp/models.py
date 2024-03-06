from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=200, null=True)
    number = models.CharField(default="", max_length=200, null=True)
    nid = models.CharField(default="", max_length=200, null=True)
    dob = models.CharField(default="dd-mm-yy", max_length=200, null=True)
    # desc_text = 'Enter your address'
    desc = models.CharField(default = '', max_length=200, null=True)
    profile_img = models.ImageField(default='media/default.jpg', upload_to='media', null='True', blank=True)


    def __str__(self):
        return f"{self.user.username}'s profile"
    




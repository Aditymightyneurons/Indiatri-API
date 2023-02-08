from django.db import models
from django.contrib.auth.models import AbstractUser



    

class User(AbstractUser):
    phone = models.TextField(max_length=13, blank=False,unique=True,null=False)
    username = models.CharField(max_length=100,unique=False)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, null=False)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS= ['username']
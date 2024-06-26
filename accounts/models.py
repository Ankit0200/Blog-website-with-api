from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class CustomUser(AbstractUser):
    username=None

    email=models.EmailField(unique=True)
    phone_no=models.CharField(max_length=12,unique=True,null=True)
    is_phone_number=models.BooleanField(default=False)
    profile_picture=models.ImageField(upload_to='profile_pictures',default='static/profile_pictures',null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ()

    objects =UserManager()

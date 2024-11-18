from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone= models.BigIntegerField(default=0)
    address = models.CharField(max_length=20,default="")
    is_superuser = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


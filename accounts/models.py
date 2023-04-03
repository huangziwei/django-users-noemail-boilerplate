from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customuser(AbstractUser):
    name = models.CharField(verbose_name="name", blank=True, max_length=255)
    bio = models.TextField("Bio", blank=True)

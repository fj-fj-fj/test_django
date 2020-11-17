from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save 
from django.dispatch import receiver


class CustomUser(AbstractUser):
    """auth/login-related fields"""

    def __str__(self):
        return self.username


# class Profile(models.Model):
#     """non-auth-related/cosmetic fields"""
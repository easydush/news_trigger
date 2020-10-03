from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model User
    """

    def __str__(self):
        return f'{self.username} - ({self.get_full_name()})'

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=150, unique=True)
    phone = models.CharField(null=True, max_length=20)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

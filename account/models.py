from django.db import models
from django.contrib.auth.models import AbstractUser



class MyUser(AbstractUser):
    pass


class EmailConfirmatiom(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=200, null=True)



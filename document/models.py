import uuid
from datetime import date
from autoslug import AutoSlugField
import uuid
from django.core.checks import messages
from django.utils.text import slugify

from django.db import models
from account.models import MyUser

# Create your models here.


class Employee(models.Model):
    Role = (
        ('Staff', 'Staff'),
        ('Others', 'Others'),
    )

    id = models.UUIDField(primary_key=True, blank=True,
                          default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        MyUser, null=True, on_delete=models.CASCADE, blank=True)
    is_admin = active = models.BooleanField(
        null=True, default=False, blank=True)
    role = models.CharField(choices=Role, max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=500, null=True)
    middle_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True)
    photo = models.ImageField(
        upload_to='prof/photos', default="defaulf-user.png", blank=True)
    company_photo = models.ImageField(
        upload_to='company/photos', default="defaulf-user.png", blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(null=True, default=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.company_name)

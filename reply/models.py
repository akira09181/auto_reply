from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=50, null=True)
    line_id = models.CharField(max_length=50)

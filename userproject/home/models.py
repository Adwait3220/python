from datetime import date
from email.headerregistry import Address
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    query=models.CharField(max_length=122)
    country=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    zip=models.CharField(max_length=122)
    date=models.DateField(max_length=122)

    def __str__(self) -> str:
        return self.name
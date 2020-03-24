from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Search(models.Model):
    query = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.query}"

# Create your models here.

class Recovery(models.Model):
    
    User = models.ForeignKey(User, on_delete=models.CASCADE)

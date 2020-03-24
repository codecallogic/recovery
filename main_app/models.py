from django.db import models
from django.contrib.auth.models import User

class Search(models.Model):
    query       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.query}"

class Symptoms(models.Model):
    s_id        = models.CharField(max_length=100)
    label       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)       

    def __str__(self):
        return f"Symptom {self.label} with id {self.s_id} is being added"
    



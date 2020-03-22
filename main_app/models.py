from django.db import models

class Search(models.Model):
    query = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.query}"

class Recovery(models.Model):
    
    User = models.ForeignKey(User, on_delete=models.CASCADE)
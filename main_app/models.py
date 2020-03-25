from django.db import models
from django.contrib.auth.models import User
from itertools import chain

class Search(models.Model):
    query       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.query}"

class Symptoms(models.Model):
    s_id        = models.CharField(max_length=100)
    label       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)   

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(self)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(self)]
        return data

    class Meta:
        unique_together = ('s_id', 'label')    

    def __str__(self):
        return f"Symptom {self.label} with id {self.s_id} is being added"
    
class Patient(models.Model):
    firstname   = models.CharField(max_length=100)
    lastname    = models.CharField(max_length=100)
    age         = models.IntegerField()
    gender      = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('firstname', 'lastname', 'age', 'gender')   

    def __str__(self):
        return f"Patient {self.firstname} {self.lastname} of age {self.age}, gender {self.gender} is submitted a form "

    

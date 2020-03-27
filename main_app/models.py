from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Tracker(models.Model):
    tracker_name    = models.CharField(max_length=100)
    label1          = models.CharField(max_length=100)
    label2          = models.CharField(max_length=100)
    label3          = models.CharField(max_length=100)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tracker_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tracker_id': self.id})

class Record(models.Model):
    input1          = models.IntegerField()
    input2          = models.IntegerField()
    input3          = models.IntegerField()
    datestamp       = models.DateField(auto_now_add=True)
    timestamp       = models.TimeField(auto_now_add=True)
    tracker         = models.ForeignKey(Tracker, on_delete=models.CASCADE)

    def __int__(self):
        return self.input1, self.input2, self.input3

    class Meta:
        ordering = ['-datestamp', '-timestamp']

class Search(models.Model):
    query       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.query}"

class Symptoms(models.Model):
    s_id        = models.CharField(max_length=100)
    label       = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)   

    class Meta:
        unique_together = ('s_id', 'label')    

    def __str__(self):
        return f"Symptom {self.label} with id {self.s_id} is being added"
    
class Patient(models.Model):
    firstname   = models.CharField(max_length=100)
    lastname    = models.CharField(max_length=100)
    age         = models.IntegerField()
    sex         = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('firstname', 'lastname', 'age', 'sex')   

    def __str__(self):
        return f"Patient {self.firstname} {self.lastname} of age {self.age}, sex {self.sex} is submitted a form "

    

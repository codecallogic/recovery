# class Patient(models.Model):
#     firstname   = models.CharField(max_length=100)
#     lastname    = models.CharField(max_length=100)
#     age         = models.DateField()
#     gender      = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Diagnosis(models.Model):
#     name        = models.CharField(max_length=100)
#     condition   = models.CharField(max_length=100)
#     probability = models.CharField(max_length=100)
#     user        = models.ForeignKey(User, on_delete=models.CASCADE)

# class Recovery(models.Model):
#     pass

# SELECT * FROM main_app_symptoms;
# for label in Symptoms.objects.values_list('label', flat=True).distinct():
#     Symptoms.objects.filter(pk__in=Symptoms.objects.filter(label=label).values_list('id', flat=True)[1:]).delete()
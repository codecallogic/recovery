# class Patient(models.Model):
#     firstname   = models.CharField(max_length=100)
#     lastname    = models.CharField(max_length=100)
#     birthdate   = models.DateField()
#     height      = models.CharField(max_length=100)
#     weight      = models.CharField(max_length=100)
#     diagnosis   = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Diagnosis(models.Model):
#     name        = models.CharField(max_length=100)
#     condition   = models.CharField(max_length=100)
#     probability = models.CharField(max_length=100)
#     user        = models.ForeignKey(User, on_delete=models.CASCADE)

# class Recovery(models.Model):
#     pass
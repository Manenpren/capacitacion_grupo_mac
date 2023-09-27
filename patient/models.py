from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name

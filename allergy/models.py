from django.db import models
from patient.models import Patient

class Allergy(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='allergies', on_delete=models.CASCADE)
    allergy_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.patient.name} - {self.allergy_name}'

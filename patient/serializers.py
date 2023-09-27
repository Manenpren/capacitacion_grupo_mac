from rest_framework import serializers
from .models import Patient
from allergy.models import Allergy

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  # O puedes especificar los campos que deseas incluir aquí

    def allergies(patient: int):
        """
        Funcion para listar todas las alergias de un paciente
        """

        allergies = Allergy.objects.filter(patient=patient)

        return allergies
from rest_framework import serializers
from .models import Allergy
from patient.models import Patient

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ['id', 'allergy_name']

class AllergiesPatientSerializer(serializers.ModelSerializer):
    allergies = AllergySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'gender', 'date_of_birth', 'address', 'allergies']

    def to_representation(self, instance):
        representacion = super().to_representation(instance)

        print(Allergy.objects.filter(patient=instance))

        representacion['allergies'] = AllergySerializer(Allergy.objects.filter(patient=instance), many=True).data

        return representacion
    
    def create(self, validate_data):
        alergias = self.context.get('allergies')
        paciente = Patient.objects.create(**validate_data)
        paciente.save()

        for alergia in alergias:
            Allergy.objects.create(patient=paciente,allergy_name=alergia.get('allergy_name'))

        return paciente

    def update(self, instance, validated_data):
        allergies_data = self.context.get('allergies')
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        # Eliminar alergias existentes
        instance.allergies.all().delete()

        # Crear alergias nuevas
        for allergy_data in allergies_data:
            Allergy.objects.create(patient=instance, **allergy_data)

        return instance
    
    def validate(self, validated_data):
        allergies = self.context.get('allergies')

        allergy_names = set()
        for allergy in allergies:
            allergy_name = allergy['allergy_name']
            if allergy_name in allergy_names:
                raise serializers.ValidationError("La alergia '{}' está duplicada en la lista.".format(allergy_name))
            allergy_names.add(allergy_name)
    
        return validated_data    

from rest_framework import serializers
from .models import Allergy

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'  # O puedes especificar los campos que deseas incluir aquí

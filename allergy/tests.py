from django.test import TestCase
from .models import Allergy
from patient.models import Patient

class AllergyModelTestCase(TestCase):
    def test_create_allergy(self):
        patient = Patient.objects.create(
            name="John Doe",
            gender="M",
            date_of_birth="1990-01-01",
            address="123 Main St"
        )
        self.assertEqual(patient.name, "John Doe")
        patient = Patient.objects.get(id=1)
        allergy = Allergy.objects.create(
            patient=patient,
            allergy_name="Polen"
        )
        self.assertEqual(allergy.allergy_name, "Polen")
        # Agrega más aserciones según sea necesario para verificar otros campos

class AllergyViewTestCase(TestCase):
    def test_allergy_list_view(self):
        response = self.client.get('/api/allergies/')
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según sea necesario para verificar la lista de alergias

    def test_allergy_detail_view(self):
        patient = Patient.objects.create(
            name="John Doe",
            gender="M",
            date_of_birth="1990-01-01",
            address="123 Main St"
        )
        self.assertEqual(patient.name, "John Doe")
        patient = Patient.objects.get(id=1)
        allergy = Allergy.objects.create(
            patient=patient,
            allergy_name="Nueces"
        )
        response = self.client.get(f'/api/allergies/{allergy.id}/')
        print('response')
        print(response)
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según sea necesario para verificar los detalles de la alergia

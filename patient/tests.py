from django.test import TestCase
from .models import Patient

class PatientModelTestCase(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(
            name="John Doe",
            gender="M",
            date_of_birth="1990-01-01",
            address="123 Main St"
        )
        self.assertEqual(patient.name, "John Doe")


class PatientViewTestCase(TestCase):
    def test_patient_list_view(self):
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, 200)


    def test_patient_detail_view(self):
        patient = Patient.objects.create(
            name="Jane Doe",
            gender="F",
            date_of_birth="1995-02-15",
            address="456 Elm St"
        )
        response = self.client.get(f'/api/patients/{patient.id}/')
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según sea necesario para verificar los detalles del paciente

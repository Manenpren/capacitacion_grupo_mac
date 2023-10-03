# En views.py de la aplicación "patient"
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm

from rest_framework import viewsets, status
from .serializers import PatientSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from allergy.models import Allergy
from allergy.serializers import AllergiesPatientSerializer

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})

def patient__allergies_list(request, pk):
    allegies = PatientSerializer.allergies(patient=pk)
    return render(request, 'patient/patient_allergies_list.html', {'allergies': allegies})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient/patient_confirm_delete.html', {'patient': patient})

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientAllergiesView(APIView):
    serializer_class = AllergiesPatientSerializer

    def get_queryset(self, id):
        return Patient.objects.filter(id=id).first()
    
    def get(self, request, id):
        response = self.serializer_class(self.get_queryset(id)).data
        return Response(response, status=status.HTTP_200_OK)
    
class PatientAllergiesViewSet(viewsets.ModelViewSet):
    serializer_class = AllergiesPatientSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        patient_id = self.kwargs['id']
        return Patient.objects.filter(id=patient_id)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(Patient, pk=kwargs['id'])
        allergies_data = request.data.get('allergies', [])  # Obtener las alergias de la solicitud (puede ser una lista vacía si no hay alergias)

        # Crear una instancia del serializador con los datos de la solicitud y las alergias en el contexto
        serializer = AllergiesPatientSerializer(instance, data=request.data, context={'allergies': allergies_data})
        
        # Validar y guardar los datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        # Obtener los datos del paciente y las alergias de la solicitud
        allergies_data = request.data.get('allergies', [])  # Suponiendo que las alergias están incluidas en el campo 'allergies'
        
        # Serializar el paciente para validar los datos
        serializer = AllergiesPatientSerializer(data=request.data, context={'allergies': allergies_data})

        # Validar y guardar los datos
        if serializer.is_valid():
            # Guardar el paciente y las alergias
            paciente = serializer.save()

            # Crear las alergias asociadas al paciente
            for allergy_data in allergies_data:
                Allergy.objects.create(patient=paciente, **allergy_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
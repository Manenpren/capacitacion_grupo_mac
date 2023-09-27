# En views.py de la aplicación "patient"
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm

from rest_framework import viewsets
from .serializers import PatientSerializer

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
# En views.py de la aplicación "allergy"
from django.shortcuts import render, get_object_or_404, redirect
from .models import Allergy
from .forms import AllergyForm

from rest_framework import viewsets
from .models import Allergy
from .serializers import AllergySerializer

def allergy_list(request):
    allergies = Allergy.objects.all()
    return render(request, 'allergy/allergy_list.html', {'allergies': allergies})

def allergy_detail(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    return render(request, 'allergy/allergy_detail.html', {'allergy': allergy})

def allergy_create(request):
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allergy_list')
    else:
        form = AllergyForm()
    return render(request, 'allergy/allergy_form.html', {'form': form})

def allergy_update(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    if request.method == 'POST':
        form = AllergyForm(request.POST, instance=allergy)
        if form.is_valid():
            form.save()
            return redirect('allergy_list')
    else:
        form = AllergyForm(instance=allergy)
    return render(request, 'allergy/allergy_form.html', {'form': form})

def allergy_delete(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    if request.method == 'POST':
        allergy.delete()
        return redirect('allergy_list')
    return render(request, 'allergy/allergy_confirm_delete.html', {'allergy': allergy})

class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
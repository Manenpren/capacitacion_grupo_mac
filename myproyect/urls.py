"""
URL configuration for myproyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from patient.views import (
    patient_detail,
    patient__allergies_list,
    patient_create,
    patient_update,
    patient_delete,
    patient_list,
    PatientViewSet,
    PatientAllergiesView,
    PatientAllergiesViewSet
)

from allergy.views import (
    allergy_list,
    allergy_detail,
    allergy_create,
    allergy_update,
    allergy_delete,
    AllergyViewSet,
)


router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'allergies', AllergyViewSet)

simple_router = routers.SimpleRouter()
simple_router.register(r'patients/(?P<id>\d+)/allergies', PatientAllergiesViewSet, basename='patient-allergies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allergies/', allergy_list, name='allergy_list'),
    path('allergies/<int:pk>/', allergy_detail, name='allergy_detail'),
    path('allergies/create/', allergy_create, name='allergy_create'),
    path('allergies/<int:pk>/update/', allergy_update, name='allergy_update'),
    path('allergies/<int:pk>/delete/', allergy_delete, name='allergy_delete'),
    path('patients/', patient_list, name='patient_list'),
    path('', patient_list, name='patient_list_root'),
    path('patients/<int:pk>/', patient_detail, name='patient_detail'),
    path('patients/<int:pk>/allergies', patient__allergies_list, name='patient_allergies_detail'),
    path('patients/create/', patient_create, name='patient_create'),
    path('patients/<int:pk>/update/', patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', patient_delete, name='patient_delete'),
    path('api/', include(router.urls)),
    path('api/', include(simple_router.urls)),
    #path('api/patients/<int:id>/allergies', PatientAllergiesView.as_view(), name='patient-allergies'),
]
"""_summary_imports"""
from django import forms
from .models import Allergy

class AllergyForm(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """
    class Meta:
        model = Allergy
        fields = ['patient', 'allergy_name']

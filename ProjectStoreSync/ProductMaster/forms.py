from django import forms
from .models import MaterialMaster


class MaterialMasterForm(forms.ModelForm):
    class Meta:
        model = MaterialMaster
        fields = [
            'materialName',
            'specifications',
            'minimum_quantity',
            'category',
            'unit',
        ]

from django import forms
from .models import firstruc

class fir_form(forms.ModelForm):
    class Meta:
        model = firstruc
        fields = fields = ['name', 'dob', 'pnr', 'gender', 'phone', 'email', 'address', 'complaint', 'description']

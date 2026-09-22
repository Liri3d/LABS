from django import forms
from .models import GasReading

class GasReadingForm(forms.ModelForm):
    class Meta:
        model = GasReading
        fields = ['meter_number', 'reading_date', 'value', 'comment']
        widgets = {
            'reading_date': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms
from .models import Search, Symptoms, Patient

class SearchForm(forms.ModelForm):
    query       = forms.CharField(widget=forms.TextInput(
        attrs   = {'class': 'form-control', 'placeholder': 'Please enter a symptom'}
    ))
    class Meta:
        model       = Search
        fields      = ['query']

class SymptomsForm(forms.ModelForm):
    class Meta:
        model       = Symptoms 
        fields      = ['s_id', 'label']

class PatientForm(forms.ModelForm):
    class Meta:
        model       = Patient
        fields      = ['firstname','lastname','age','gender']

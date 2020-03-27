from django.forms import ModelForm
from django import forms
from .models import Search, Symptoms, Patient, Record, Tracker

class TrackerForm(ModelForm):
    class Meta:
        model           = Tracker
        fields          = ['tracker_name', 'label1', 'label2', 'label3']

class RecordForm(ModelForm):
    class Meta:
        model           = Record
        fields          = ['input1', 'input2', 'input3']

class SearchForm(forms.ModelForm):
    query           = forms.CharField(widget=forms.TextInput(
        attrs       = {'class': 'form-control', 'placeholder': 'Please enter a symptom'}
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
        fields      = ['firstname','lastname','age','sex']
